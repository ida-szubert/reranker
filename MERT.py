#!/usr/bin/env python
import optparse
import bleu
import os
import matplotlib.pylab as pl
import numpy as np
import random

optparser = optparse.OptionParser()
optparser.add_option("-t", "--kbest-training-list", dest="training_input", default="data/train.100best", help="100-best training translation lists")
optparser.add_option("-r", "--reference", dest="reference", default="data/train.ref", help="Training target language reference sentences")
optparser.add_option("-k", "--kbest-list", dest="input", default="data/dev+test.100best", help="100-best testing translation lists")
(opts, _) = optparser.parse_args()


def get_reference_sentences():
	return [line.strip().split() for line in open(opts.reference)]

def get_candidate_translations():
	return [hyp.split(' ||| ') for hyp in open(opts.training_input)]

def update_param(feature, current_param_dict):
	sentence_dict = {}
	for m in xrange(0, num_sents):
		ref = reference[m]
		candidates = all_hyps[m * 100:m * 100 + 100]
		line_dict, steepest_line = define_sentence_lines(feature, candidates, current_param_dict)
		# to see the lines on a graph
		#xs = np.array(range(-1000, 1000))
		#for id in line_dict:
		#	line = line_dict[id]
		#	y = [x*line[0]+line[1] for x in xs]
		#	pl.plot(xs, y)
		#pl.savefig('foo.png')
		# end of graph part
		sequence = find_line_sequence(line_dict, [(steepest_line, -999999)])
		interval_stats_dict = {}
		for candidate, interval_start, interval_end in sequence:
			interval_stats_dict[(interval_start, interval_end)] = list(bleu.bleu_stats(candidate[2].split(), ref))
		sentence_dict[m] = interval_stats_dict

	all_interval_ends = sorted(set([item[1] for sublist in [dict.keys() for dict in sentence_dict.values()] for item in sublist]))
	best_interval, best_BLEU = choose_best_interval(all_interval_ends, sentence_dict)
	return_param_dict = {}
	for f in current_param_dict:
		return_param_dict[f] = current_param_dict[f] if f != feature else sum(best_interval)/2
	return return_param_dict, best_BLEU

def choose_best_interval(interval_ends, sentence_dict):
	current_best = 0
	best_interval = (0,0)
	for i in range(len(interval_ends)):
		all_stats = collect_BLEU_stats(sentence_dict, interval_ends[i])
		new_BLEU = 100*bleu.bleu(all_stats)
		if new_BLEU > current_best:
			current_best = new_BLEU
			best_interval = (interval_ends[i-1], interval_ends[i])
	return best_interval, current_best

def collect_BLEU_stats(iter_dict, interval_end):
	all_stats = [0 for j in xrange(10)]
	for m in iter_dict:
		sentence_stats = [iter_dict[m][k] for k in iter_dict[m].keys() if k[0] < interval_end <= k[1]][0]
		all_stats = [sum(scores) for scores in zip(all_stats, sentence_stats)]
	return all_stats

def define_sentence_lines(target_feature, candidates, current_param_dict):
	sentence_lines = {}
	steepest_line = (99999, 0, [])
	for (n, (num, hyp, feats)) in enumerate(candidates):
		b = 0.0
		a = 0.0
		for feat in feats.split(' '):
			k, v = feat.split('=')
			if k == target_feature:
				a = float(v)
			else:
				b += float(v)*current_param_dict[k]
		sentence_lines[n] = (a, b, hyp)
		if a < steepest_line[0]:
			steepest_line = (a, b, hyp)
	return sentence_lines, steepest_line

def find_line_sequence(line_dict, sequence):
	current_line = sequence[-1][0]
	current_intercept = sequence[-1][1]
	next = find_next_line(current_line, line_dict, current_intercept)
	if next[1] == 999999:
		sequence[-1] = (current_line, current_intercept, 999999)
		return sequence
	else:
		sequence[-1] = (current_line, current_intercept, next[1])
		sequence.append(next)
		return find_line_sequence(line_dict, sequence)

def find_next_line(current_line, line_dict, last_intercept):
	next_line = current_line
	next_intercept = 999999
	for id in line_dict:
		if line_dict[id] != current_line:
			intercept = get_intercept(current_line, line_dict[id])
			if last_intercept < intercept < next_intercept:
				next_intercept = intercept
				next_line = line_dict[id]
	return next_line, next_intercept

def get_intercept(line1, line2):
	if line1[0] - line2[0]:
		return (line2[1] - line1[1]) / (line1[0] - line2[0])
	else:
		return -1000000

reference = get_reference_sentences()
all_hyps = get_candidate_translations()
num_sents = len(reference)

param_dict = {}
best_BLEU = 0

for n in range(0,10):
	run_param_dict = {}
	_, _, feats = all_hyps[0]
	for feat in feats.split():
		k,_ = feat.split('=')
		run_param_dict[k] = random.randint(-10, 10)
		initial_weights = ' '.join(["{}={}".format(feat, run_param_dict[feat]) for feat in run_param_dict])

	update_order = random.sample(run_param_dict.keys(), len(run_param_dict.keys()))
	previous_BLEU = 0
	current_BLEU = 1
	iteration = 0
	last_updated = ''
	to_update = [f for f in update_order if f != last_updated]

	while current_BLEU - previous_BLEU > 0.0001:
		previous_BLEU = current_BLEU
		improvements = [(feat, update_param(feat, run_param_dict)) for feat in to_update]
		best = sorted(improvements, key=lambda x: x[1][1])[-1]
		current_BLEU = best[1][1]
		run_param_dict = best[1][0]
		last_updated = best[0]
		iteration += 1

	if current_BLEU > best_BLEU:
		param_dict = run_param_dict
		best_BLEU = current_BLEU

#print 'Initial weights: {}'.format(initial_weights)
weights = ' '.join(["{}={}".format(feat, param_dict[feat]) for feat in param_dict])
os.system("python rerank -k {} -w '{}'".format(opts.input, weights))
#print iteration
print best_BLEU