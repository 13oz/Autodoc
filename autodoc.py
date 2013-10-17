#! /usr/bin/python
__author__ = 'Duminsky Nick'
import os
import sys
import argparse

import reader
import walker

parser = argparse.ArgumentParser(description='foo')

parser.add_argument('-c', '--config', help='path to config file', required=False)
parser.add_argument('-t', '--target', help='target file or directory', required=False)
parser.add_argument('-l', '--log', help='log file name', default=sys.stdout, required=False)
parser.add_argument('-i', '--intend', help='intend style', default='space', required=False)


def main():
    target_path = parser.parse_args().target
    #log_file = parser.parse_args().log

    #check OS
    if os.name == 'nt':
        #this is Windows, so let's have some sex with path...
        target_path = target_path.replace("\\", "/")
        #log_file = log_file.replace("\\", "/")

    if os.path.isfile(target_path):
        reader.read_file(target_path)
    elif os.path.isdir(target_path):
        walker.walk_through(target_path)
    else: print(parser.description)

if __name__ == "__main__":
    main()