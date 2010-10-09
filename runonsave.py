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

import os, sys, subprocess, time

SCAN_INTERVAL=10
EXCLUDES=['.git', '.hg', 'CVS']

def main ():
  cwd = os.getcwd()
  last_run=os.path.getmtime(cwd)
  while(True):
    last_modified=get_last_modified(cwd)
    if (last_modified > last_run):
      print "*** Save detected - running command ***"
      args=sys.argv
      
      #strip out the python command
      if args[0] is "python":
        args=args[1:]
      args=args[1:]

      subprocess.Popen(args)
      last_run=last_modified
    time.sleep(SCAN_INTERVAL)

def get_last_modified(current_dir):
    """Recurses though a directory tree and finds the newest last modified date"""
    last_modified=os.path.getmtime(current_dir)
    subdirs=os.listdir(current_dir)
    subdirs = [subdir for subdir in subdirs if should_check(subdir)]

    for subdir in subdirs:
      temp_last_modified=get_last_modified(subdir)
      if(temp_last_modified>last_modified):
        last_modified=temp_last_modified

    return last_modified

def should_check(path):
  """Checks if path should be recursively searched. Excludes files and SCM dirs"""
  if(os.path.isdir(path)):
    basename=os.path.basename(path)
    if basename not in EXCLUDES:
      return True

  return False

if __name__ == '__main__':
  main()

