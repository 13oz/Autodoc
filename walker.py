import os
import sys

import reader

def walkThrough(folder, errFile=sy.stdout):
	for dir in [dir for dir in os.listdir(folder) if os.path.isdir(dir)]:
		for file in [file for file in os.listdir(folder) if (os.path.isfile(file) and checkFile(file))]:
			reader.readFile(file)
		for elem in [elem for elem in os.listdir(dir) if os.path.isdir(elem)]: walkThrough(elem)

"""def checkFolder(folder, errFile=sys.stdout):
	for file in [file for file in os.listdir(folder) if (os.path.isfile(file) and checkFile(file))]:
		reader.readFile(file)
	for file in os.listdir(folder):
					if os.path.isdir(folder+"/"+file):
						walkThrough(folder+"/"+file, errFile)
					if os.path.isfile(folder+"/"+file):
						if checkFile(folder+"/"+file, errFile):
							reader.readFile(folder+"/"+file, errFile)"""

def checkFile(filename, errFile=sys.stdout):
	if filename.endswith(".py"):
		return True
	else: 
		return False