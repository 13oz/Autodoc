import os
import sys
import argparse

import reader
import walker

parser = argparse.ArgumentParser(description='foo')

parser.add_argument('-t', '--target', help='target file or directory', required=False)
parser.add_argument('-l', '--log', help='log file name', default=sys.stdout, required=False)

args = parser.parse_args()

if os.path.isfile(args.target):
	
	reader.readFile(args.target.replace("\\", "/"), args.log)
elif os.path.isdir(args.target):
	walker.walkThrough(args.target.replace("\\", "/"))
else: print(parser.description)