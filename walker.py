import os
import reader
import sys

#$special comment

#проверка была вынесена в autodoc.py
"""def isDir(folder):
	if os.path.isdir(folder):
		walkThrough(folder)
	else:
		print(folder+" is not a folder!")"""

def walkThrough(folder, errFile=sys.stdout):
	for file in os.listdir(folder):
		if os.path.isdir(folder+"/"+file):
			walkThrough(folder+"/"+file, errFile)
		if os.path.isfile(folder+"/"+file):
			if checkFile(folder+"/"+file, errFile):
				reader.readFile(folder+"/"+file, errFile)

def checkFile(filename, errFile):
	if filename.endswith(".py"):
		return True
	else: 
		print(filename+" is not a python source code!", file=errFile)
		return False