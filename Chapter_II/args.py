#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Example of command line argument passing.

Usage:
	python args.py [String]
	
The program uses a function to print user greetings.
@author Dragos STOICA
@version 0.1
@date 08.mar.2018
"""

import sys

def usage():
    """Help on how to use the program"""
    print ("""
    The program must be called with at least one argument of type string
    python args.py Dragos
    """
    )

def greetings(personName="Not Sure"):
    """Print greetings for person name received as input value"""
    print("Welcome to the world of Python - ", personName, "!")

def main(argv=None):
    """The main function: check the input arguments and do the business logic"""
    if argv is None:
        argv = sys.argv

    if len(argv) == 1:
        usage()
    else:
        #do the program logic
        greetings(argv[1])

    return 0	

if __name__ == "__main__":
    sys.exit(main())