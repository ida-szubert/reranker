parameters = [x,y,z]
previous_BLEU = 0
paramX = choose_randomly(initial_parameters)
current_BLEU = update_paramX(paramX)
if (current_BLEU - previous_BLEU) < 0.1:
	stop
else;
	keep looking

def update_paramX()
for paramX:
	paramX_dict = {}
	for Russian_sentence:
		for candidate:
			b = y*feature2 + z* feature3
			a = feature1
			dictionary[candidate] = (a,b)
		intercept_list = []
		first_s = steepest_slope
		sequence = find_line_sequence(first_s, line_dict, -999999, [])
		interval_dict = {}
		for interval in sequence:
			interval_dict[interval] = blue.blue_stats(interval[candidate], Russian_sentence)
		paramX_dict[Russian_sentence] = interval_dict
	all_intervals = sorted([Russian.keys() for Russsian in paramX_dict])
	BLEU_list = []
	for interval in all_intervals:
		all_stats = [0 for i in xrange(10)]
		for Russsian in paramX_dict:
			sentence_stats = choose_interval(interval)
			add(sentence_stats, all_stats)
		BLEU_list.append(bleu.bleu(all_stats))
	min(BLEU_list)

def find_line_sequence(current_s, line_dict, current_intercept, sequence):
	next= find_next_line(current_s, line_dict, current_intercept)
	if next:
		sequence.append(next)
		find_line_sequence(next, line_dict, sequence)
	else:
		return sequence


def find_next_line(current, line_dict, last_intercept):
	intercept_dict = {}
	for line in line_dict:
		intercept_dict[line] = get_intercept(current, line)
	if min(intercept_dict) > last_intercept:
		new_line = min(intercept_dict)
	    return (new_line, intercept_point)
	else:
		return None