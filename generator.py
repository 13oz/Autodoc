import os
import sys
import xml.etree.ElementTree as ET

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
	print(srcfile)
	curLevel = 0
	try:
		resXML = ET.Element(os.path.basename(srcfile))
		#res=open(createName(srcfile), "w")
		for line in open(srcfile, 'r'):
			if reader.readLine(line)!=None: 
				if line(1) == curLevel
		#res.close
	except IOError:
		print("An error occured while processing "+filename, file=errFile)
		res.close()

def addSub(rootElement, subElement):
