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

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  global summary
  global fout
  fin = open(filename, "r")

  finText = fin.read()
  ans = []
  yearFound = re.search(r'<h3 align="center">Popularity\sin\s(\d\d\d\d)</h3>' ,finText)
  if yearFound:
      year = yearFound.group(1)
  else:
      if summary == True:
          print("file = ", filename, "year not found", file = fout)
      else:
          print("file = ", filename, "year not found")
      return -1

  ans.append(year)

  m = re.findall(r'<td>(\d+)</td><td>([A-Z][a-z]+)</td><td>([A-Z][a-z]+)</td>', finText)
  if not m:
      if summary == True:
          print("file = ", filename, "names not found", file = fout)
      else:
          print("file = ", filename, "names not found")
      return -1

  namesRank = {}
  for x in m:
      namesRank[x[1]] = x[0]
      namesRank[x[2]] = x[0]

  for l in sorted(namesRank.keys()):
      ans.append(str(str(l) + ' ' + str(namesRank[l])))

  if summary:
      print("file = ", filename, '\t', ans, '\n', '\n', file = fout)
  else:
      print("file = ", filename, '\t', '\n', '\n', ans)
  return


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  global summary
  global fout
  if not args:
      print ('usage: [--summaryfile] file [file ...]')
      sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
      summary = True
      del args[0]

  if len(args) < 2 and summary:
      print ('usage: [--summaryfile] file [file ...]')
      sys.exit(1)

  x = 0
  if summary:
      #print(args[0])
      fout = open(args[0], "a")
      x = 1



  for i in range(x, len(args)):
      extract_names(args[i])



  #extract_names("baby2006.html")
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file

if __name__ == '__main__':
  main()
