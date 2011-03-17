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
import commands

def findspecial(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        match = re.search(r'__.+__', filename)
        if match != False:
            print os.path.abspath(os.path.join(dir, filename)


def main():
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
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
  
    rundir = ''
    if args[0] == '--run':
        rundir = args[1]
        findspecial(rundir)
        del args[0:2]

    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

  # +++your code here+++
  # Call your functions
  
if __name__ == "__main__":
    main()
