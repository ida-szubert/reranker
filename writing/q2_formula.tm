<TeXmacs|1.99.2>

<style|<tuple|generic|british>>

<\body>
  <math|h<around*|(|0\<nocomma\>,e|)>=<choice|<tformat|<table|<row|<cell|1\<nocomma\>,if
  <space|0.2spc> e=START>>|<row|<cell|0\<nocomma\>,otherwise>>>>>>

  <\eqnarray>
    <tformat|<table|<row|<cell|h<around*|(|j,e|)>=>|<cell|<below|argmax|h<around*|(|i,e<rprime|'>|)>
    e<rsub|1>\<ldots\>e<rsub|k> e<rsub|k+1>\<ldots\>e<rsub|m>e><rsub|>>|<cell|p<around*|(|h<around*|(|i,e<rprime|'>|)>|)>>>|<row|<cell|>|<cell|+>|<cell|log
    p<rsub|TM><around*|(|f<rsub|i+1>\<ldots\>f<rsub|c>\|e<rsub|k+1>\<ldots\>e<rsub|m>e|)>>>|<row|<cell|>|<cell|\<noplus\>+>|<cell|log
    p<rsub|TM><around*|(|f<rsub|c+1>\<ldots\>f<rsub|j>\|e<rsub|1>\<ldots\>e<rsub|k>|)>>>|<row|<cell|>|<cell|\<upl\>>|<cell|log
    p<rsub|LM><around*|(|e<rsub|1>\|e<rprime|'>|)>+<big|sum><rsub|k<rprime|'>=1><rsup|m-1>log
    p<rsub|LM><around*|(|e<rsub|k<rprime|'>+1>\|e<rsub|k<rprime|'>>|)>+log
    p<rsub|LM><around*|(|e\|e<rsub|m>|)>>>>>
  </eqnarray>

  with <math|0\<leq\>i\<less\>c\<leq\>j>, <math|0\<leq\>k\<leq\>m>,
  <math|e<rprime|'>\<in\>V<rsub|E>>, <math|e<rsub|1>\<ldots\>e<rsub|k>\<in\>t<around*|(|f<rsub|c+1>\<ldots\>f<rsub|j>|)>\<cup\><around*|{|\<varepsilon\>|}>>,<next-line>and
  <math|e<rsub|k+1>\<ldots\>e<rsub|m>e\<in\>t<around*|(|f<rsub|i+1>\<ldots\>f<rsub|c>|)>>.
</body>

<\initial>
  <\collection>
    <associate|font-base-size|12>
  </collection>
</initial>