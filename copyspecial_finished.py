#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
#import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them


def show_spec(directory):
    ans = []
    dir = os.listdir(directory)
    for i in dir:
        jk = re.search(r'__(\w+)__', i)
        if jk:
            ans.append(os.path.abspath(os.path.join(directory, i)))

    return ans

def to_dir(list, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)
    for i in list:
        fname = os.path.basename(i)
        shutil.copy(i, os.path.join(dest, fname))
    return

def to_zip(list, dest):
    comm = "zip -j " + dest + ' ' + ' '.join(list)
    print("im going to do:", comm)

    os.system(comm)
    




def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
      print ("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
      sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
      todir = args[1]
      del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
      tozip = args[1]
      del args[0:2]


  if len(args) == 0:
      print ("error: must specify one or more dirs")
      sys.exit(1)

  spec_files = []
  for i in args:
      spec_files.extend(show_spec(i))

  if todir:
      copy_to(spec_files, todir)
  elif tozip:
      to_zip(spec_files, tozip)
  else:
      print('\n'.join(spec_files))
      print(spec_files)


  # +++your code here+++
  # Call your functions

if __name__ == "__main__":
  main()
