import os
import sys

import generator

def walkThrough(folder, errFile=sys.stdout):
	for elem in os.listdir(folder):
		if os.path.isfile(folder+elem) & checkFile(folder+elem): 
			generator.writeToFile(folder+elem)
		elif os.path.isdir(folder+elem):
			walkThrough(folder+elem)

def checkFile(filename, errFile=sys.stdout):
	if filename.endswith(".py"):
		return True
	else: 
		return False