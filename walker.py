import os
import sys

import reader

def walkThrough(folder, errFile=sys.stdout):
	for file in os.listdir(folder):
		if os.path.isdir(folder+"/"+file):
			walkThrough(folder+"/"+file, errFile)
		if os.path.isfile(folder+"/"+file):
			if checkFile(folder+"/"+file, errFile):
				reader.readFile(folder+"/"+file, errFile)

def checkFile(filename, errFile=sys.stdout):
	if filename.endswith(".py"):
		return True
	else: 
		print(filename+" is not a python source code!", file=errFile)
		return False