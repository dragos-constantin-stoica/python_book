#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Example of console input.

Usage:
	python user_input.py
	
The program reads user input from console.
@author Dragos STOICA
@version 0.1
@date 10.oct.2020
"""

import sys
import datetime


def usage():
    """Help on how to use the program"""
    print ("""
    The program can process the following commands:
    exit - gracefully terminate the program
    time - display the current date and time on the machine
    help - display program usage details
    """
    )

def main():
  var = input("Enter your command: ")
  if var == 'exit':
      #Exit the program
      return 0
  elif var == 'help':
      #Display usage
      usage()
  elif var == 'time':
      #Display time on the host
      now = datetime.datetime.now()
      print ("Current date and time : ")
      print (now.strftime("%Y-%m-%d %H:%M:%S"))
  else : 
    print("Type help to see available commands.")
  # Recursive call of main function
  main()

if __name__ == "__main__":
    sys.exit(main())
