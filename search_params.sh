#!/usr/bin/env sh

pe="-5 -4 -3 -2 -1 0 1 2 3 4 5"
pef="-5 -4 -3 -2 -1 0 1 2 3 4 5"
plex="-5 -4 -3 -2 -1 0 1 2 3 4 5"

echo "p(e);p(e|f);p_lex(f|e);bleu" >> workdir/param_search
for par1 in $pe
do
    for par2 in $pef
    do
        for par3 in $plex
        do
            echo "${par1};${par2};${par3};" >> workdir/param_search
            python ./rerank -w "p(e)=${par1} p(e|f)=${par2} p_lex(f|e)=${par3}" >> workdir/reorder_${par1}_${par2}_${par3}.out
            python ./compute-bleu < workdir/reorder_${par1}_${par2}_${par3}.out >> workdir/param_search
        done    
    done
done

