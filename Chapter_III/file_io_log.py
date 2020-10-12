#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Example of file Input/Output.

Usage:
	python file_io.py input_file.txt
	
The program reads a text file and counts Ms/Mrs/Mr. and logs the activity in file_io.log file
@author Dragos STOICA
@version 0.1
@date 10.oct.2020
"""

import logging
import sys
from logging.handlers import TimedRotatingFileHandler
FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = "file_io.log"

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

def get_console_handler():
   console_handler = logging.StreamHandler(sys.stdout)
   console_handler.setFormatter(FORMATTER)
   return console_handler
def get_file_handler():
   file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
   file_handler.setFormatter(FORMATTER)
   return file_handler
def get_logger(logger_name):
   logger = logging.getLogger(logger_name)
   logger.setLevel(logging.DEBUG) # better to have too much log than not enough
   # logger.addHandler(get_console_handler())
   logger.addHandler(get_file_handler())
   # with this pattern, it's rarely necessary to propagate the error up to parent
   logger.propagate = False
   return logger

def main(argv=None):
  my_logger = get_logger("file_io")

  if argv is None:
    argv = sys.argv
    my_logger.debug(argv)

  if len(argv) <= 1:
      usage()
      my_logger.error("incorrect usage - the input file name not provided!")
  else:
    persons = {"Ms.":0, "Mrs.":0, "Mr.":0}
    with open(argv[1],'r') as f:
    #Read each line from the text file
      for line in f:
        #Perform action with the content of the line
        if line.find("Ms.") == 0:
          persons['Ms.'] += 1
          my_logger.info("Ms. found")
        elif line.find("Mrs.") == 0:
          persons['Mrs.'] += 1
          my_logger.info("Mrs. found")
        elif line.find("Mr.") == 0:
          persons['Mr.'] += 1
          my_logger.info("Mr. found")
        else:
          print (line, " not recognized :(")
          my_logger.error("title not recognized!")
    print(persons)


if __name__ == "__main__":
    sys.exit(main())

