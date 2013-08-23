#!/usr/bin/python
# URL that generated this code:
# http://txt2re.com/index-python.php3?s=%3Ctr%20align=%22right%22%3E%3Ctd%3E1%3C/td%3E%3Ctd%3EMichael%3C/td%3E%3Ctd%3EJessica%3C/td%3E&35&4&3

import re

txt='<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>'

re1='.*?'	# Non-greedy match on filler
re2='(\\d+)'	# Integer Number 1
re3='.*?'	# Non-greedy match on filler
re4='(?:[a-z][a-z]+)'	# Uninteresting: word
re5='.*?'	# Non-greedy match on filler
re6='(?:[a-z][a-z]+)'	# Uninteresting: word
re7='.*?'	# Non-greedy match on filler
re8='((?:[a-z][a-z]+))'	# Word 1
re9='.*?'	# Non-greedy match on filler
re10='(?:[a-z][a-z]+)'	# Uninteresting: word
re11='.*?'	# Non-greedy match on filler
re12='(?:[a-z][a-z]+)'	# Uninteresting: word
re13='.*?'	# Non-greedy match on filler
re14='((?:[a-z][a-z]+))'	# Word 2

rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13+re14,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:
    int1=m.group(1)
    word1=m.group(2)
    word2=m.group(3)
    print "("+int1+")"+"("+word1+")"+"("+word2+")"+"\n"

#-----
# Paste the code into a new python file. Then in Unix:'
# $ python x.py 
#-----

 