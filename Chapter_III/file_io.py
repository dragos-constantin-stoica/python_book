#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Example of file Input/Output.

Usage:
	python file_io.py input_file.txt
	
The program reads a text file and counts Ms/Mrs/Mr.
@author Dragos STOICA
@version 0.1
@date 10.oct.2020
"""

import sys

def usage():
    """Help on how to use the program"""
    print ("""
    The program reads a text file. On each line we may have a Ms./Mrs./Mr. and the full name.
    The program will count for each title the number of
    persons and displays the result.

    Usage:
      python file_io.py input_file.txt
    """
    )


def main(argv=None):
  if argv is None:
    argv = sys.argv

  if len(argv) <= 1:
      usage()
  else:
    persons = {"Ms.":0, "Mrs.":0, "Mr.":0}
    with open(argv[1],'r') as f:
    #Read each line from the text file
      for line in f:
        #Perform action with the content of the line
        if line.find("Ms.") == 0:
          persons['Ms.'] += 1
        elif line.find("Mrs.") == 0:
          persons['Mrs.'] += 1
        elif line.find("Mr.") == 0:
          persons['Mr.'] += 1
        else:
          print (line, " not recognized :(")
    print(persons)


if __name__ == "__main__":
    sys.exit(main())

