import argparse
import os
import reader
import walker

parser = argparse.ArgumentParser(description='foo')

parser.add_argument('-f', '--filename', help='input filename', required=False)
parser.add_argument('-d', '--dirname', help='input dir name', required=False)

args = parser.parse_args()

if args.filename:
	reader.readFile(args.filename.replace("\\", "/"))
elif args.dirname:
	walker.isDir(args.dirname.replace("\\", "/"))
else: print(parser.description)