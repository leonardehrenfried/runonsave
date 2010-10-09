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
    last_modified=os.path.getmtime(cwd)
    if (last_modified > last_run):
      print "*** Save detected - running command ***"
      subprocess.Popen(['pdflatex', 'cv.tex', ])
      last_run=last_modified
    time.sleep(SCAN_INTERVAL)

if __name__ == '__main__':
  main()

