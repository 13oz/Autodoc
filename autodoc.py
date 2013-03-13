import argparse
import os
import reader
import walker

parser = argparse.ArgumentParser(description='foo')

"""parser.add_argument('-f', '--filename', help='input filename', required=False)
parser.add_argument('-d', '--dirname', help='input dir name', required=False)"""
parser.add_argument('-t', '--target', help='target file or directory', required=False)
parser.add_argument('-l', '--log', help='log file name', required=False)

args = parser.parse_args()

#print(args, file=args.log)

if os.path.isfile(args.target):
	reader.readFile(args.target.replace("\\", "/"), open(args.log, 'w'))
elif os.path.isdir(args.target):
	walker.walkThrough(args.target.replace("\\", "/"), open(args.log, 'w'))
else: print(parser.description)