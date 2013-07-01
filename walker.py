import os
import sys

import reader

def walkThrough(folder, errFile=sys.stdout):
	for (path, dirs, files) in os.walk():
		if checkFile(files):
			reader.readFile(files)


def checkFile(filename, errFile=sys.stdout):
	if filename.endswith(".py"):
		return True
	else: 
		return False