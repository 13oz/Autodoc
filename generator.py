import os

import reader

DIR_NAME = "autodoc"

TRAILER = """\n\n\nThis documentation file was generated with help of AutoDoc software by Nick Duminsky aka 13oz ,
if ypu want to send bugreport, tell me, what you want to see in next version, or just give me advice, 
mailto: duminsky.nick@gmail.com"""

def makeFolder():
	if not os.path.exists(DIR_NAME):
		os.mkdir(DIR_NAME)

def createName(filename):
	return (filename[:-3] + ".txt")

def writeToFile(srcfile, errFile=sys.stdout):
	try:
		res=open(createFile(srcfile), "w")
		for line in reader.readFile(srcfile):
			
		res.close
	except IOError:
		print("An error occured while processing "+filename, file=errFile)
		res.close()