#!/usr/bin/python
# URL that generated this code:
# http://txt2re.com/index-python.php3?s=%3Ctr%20align=%22right%22%3E%3Ctd%3E3%3C/td%3E%3Ctd%3EMatthew%3C/td%3E%3Ctd%3EBrittany%3C/td%3E&-1&-14&35&-7&-15&5&-8&-16&2&-9

import re

txt='<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>'

re1='(
)'	# Tag 2 re3='(\\d+)'	# Integer Number 1 re4='(<\\/td>)'	# Tag 3 re5='(	)'	# Tag 4 re6='((?:[a-z][a-z]+))'	# Word 1 re7='(<\\/td>)'	# Tag 5 re8='(	)'	# Tag 6 re9='((?:[a-z][a-z]+))'	# Word 2 re10='(<\\/td>)'	# Tag 7 rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10,re.IGNORECASE|re.DOTALL) m = rg.search(txt) if m:     tag1=m.group(1)     tag2=m.group(2)     int1=m.group(3)     tag3=m.group(4)     tag4=m.group(5)     word1=m.group(6)     tag5=m.group(7)     tag6=m.group(8)     word2=m.group(9)     tag7=m.group(10)     print "("+tag1+")"+"("+tag2+")"+"("+int1+")"+"("+tag3+")"+"("+tag4+")"+"("+word1+")"+"("+tag5+")"+"("+tag6+")"+"("+word2+")"+"("+tag7+")"+"\n" #----- # Paste the code into a new python file. Then in Unix:' # $ python x.py #-----
 