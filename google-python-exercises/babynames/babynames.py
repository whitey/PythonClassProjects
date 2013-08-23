#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def isYear(line):
  year = re.search(r'Popularity in ....',line)
  if year: return year.group()

def isBabyNames(line):
  re1='.*?' # Non-greedy match on filler
  re2='(\\d+)'  # Integer Number 1
  re3='.*?' # Non-greedy match on filler
  re4='(?:[a-z][a-z]+)' # Uninteresting: word
  re5='.*?' # Non-greedy match on filler
  re6='(?:[a-z][a-z]+)' # Uninteresting: word
  re7='.*?' # Non-greedy match on filler
  re8='((?:[a-z][a-z]+))' # Word 1
  re9='.*?' # Non-greedy match on filler
  re10='(?:[a-z][a-z]+)'  # Uninteresting: word
  re11='.*?'  # Non-greedy match on filler
  re12='(?:[a-z][a-z]+)'  # Uninteresting: word
  re13='.*?'  # Non-greedy match on filler
  re14='((?:[a-z][a-z]+))'  # Word 2

  rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13+re14,re.IGNORECASE|re.DOTALL)
  m = rg.search(txt)
  if m:
    rank=m.group(1)
    boyName=m.group(2)
    girlName=m.group(3)



def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  file = open(filename, 'r')
  for line in file:
    year = re.search(r'Popularity in ....',line)

    re1='.*?' # Non-greedy match on filler
    #re2='(\\d+)'  # Rank
    re2=([0-9][0-9][0-9]|1000) # Rank
    re3='.*?' # Non-greedy match on filler
    re4='(?:[a-z][a-z]+)' # Uninteresting: word
    re5='.*?' # Non-greedy match on filler
    re6='(?:[a-z][a-z]+)' # Uninteresting: word
    re7='.*?' # Non-greedy match on filler
    re8='((?:[a-z][a-z]+))' # Boy Name 1
    re9='.*?' # Non-greedy match on filler
    re10='(?:[a-z][a-z]+)'  # Uninteresting: word
    re11='.*?'  # Non-greedy match on filler
    re12='(?:[a-z][a-z]+)'  # Uninteresting: word
    re13='.*?'  # Non-greedy match on filler
    re14='((?:[a-z][a-z]+))'  # Girl Name 2

    rg = re.compile(re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13+re14,re.IGNORECASE|re.DOTALL)
    m = rg.search(line)

    #################
    if year:
      print year.group()
    elif m:
      rank = m.group(1)
      boyName = m.group(2)
      girlName = m.group(3)
      print rank + " " + boyName + " " + girlName
    #print line
  file.close()
  return


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

  extract_names("baby1990.html")
  
if __name__ == '__main__':
  main()
