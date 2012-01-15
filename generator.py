import os

DIR_NAME = "autodoc"

def makeFolder():
	if not os.path.exists(DIR_NAME):
		os.mkdir(DIR_NAME)

def writeToFile(filename, text):
	try:
		res=open(filename, "w", encoding="utf8")
		res.write(text+"\n")
	except IOError:
		print("An error occured while processing "+filename, file=sys.stderr)
	finally:
		res.close()

def formFileName(filename):
	return (filename[:-3] + ".txt")