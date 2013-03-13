import os

DIR_NAME = "autodoc"

def makeFolder():
	if not os.path.exists(DIR_NAME):
		os.mkdir(DIR_NAME)

def writeToFile(filename, text, errFile):
	try:
		res=open(filename, "w")
		res.write(text+"\n")
		res.close
	except IOError:
		print("An error occured while processing "+filename, file=errFile)
		res.close()
		

def formFileName(filename):
	return (filename[:-3] + ".txt")