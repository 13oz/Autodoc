import os
import reader

#$special comment

def isDir(folder):
	if os.path.isdir(folder):
		walkThrough(folder)
	else:
		print(folder+" is not a folder!", file=sys.stderr)

def walkThrough(folder):
	for file in os.listdir(folder):
		if os.path.isdir(folder+"/"+file):
			walkThrough(folder+"/"+file)
		if os.path.isfile(folder+"/"+file):
			if checkFile(folder+"/"+file):
				reader.readFile(folder+"/"+file)

def checkFile(filename):
	if filename.endswith(".py"):
		return True
	else: return False