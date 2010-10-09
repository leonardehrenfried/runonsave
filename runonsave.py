#!/usr/bin/env python
"""
SYNOPSIS

    TODO helloworld [-h,--help] [-v,--verbose] [--version]

DESCRIPTION

    Runs a command when a file in the current working directory is changed

EXAMPLES

    TODO: Show some examples of how to use this script.

EXIT STATUS

    TODO: List exit codes

AUTHOR

    Leonard Ehrenfried <leonard.ehrenfried@web.de>

"""

import os
import subprocess
import time
import re

SCAN_INTERVAL=10

def main ():
  cwd = os.getcwd()
  last_run=os.path.getmtime(cwd)
  while(True):
    last_modified=get_last_modified(cwd)
    if (last_modified > last_run):
      print "*** Save detected - running command ***"
      subprocess.Popen(['pdflatex', 'cv.tex', ])
      last_run=last_modified
    time.sleep(SCAN_INTERVAL)

def get_last_modified(current_dir):
    """Recurses though a directory tree and finds the newest last modified date"""
    last_modified=os.path.getmtime(current_dir)
    print "checking %s: " % current_dir
    subdirs=os.listdir(current_dir)

    for subdir in subdirs:
      if(os.path.isdir(subdir)):
        temp_last_modified=get_last_modified(subdir)
        if(temp_last_modified>last_modified):
          last_modified=temp_last_modified

    return last_modified


if __name__ == '__main__':
  main()

