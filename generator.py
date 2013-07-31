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

def getRightElement(element):
	return list(element[len(list(element))-1])

def findParent(root, srcLine):
	curElem = root
	for i in range(srcLine[0]):
		curElem = getRightElement(curElem)
	return curElem

def writeToFile(srcfile, errFile=sys.stdout):
	print(srcfile)
	root = ET.Element(os.path.basename(srcfile)) 
	try:
		for line in open(srcfile):
			resLine = reader.readLine(line)
			if resLine != None:
				print(resLine)
				elem = ET.SubElement(findParent((root), resLine), resLine[1])
		tree = ET.ElementTree(root)
		tree.write(srcfile.replace('.py', '.xml'))
	except IOError:
		print("An error occured while processing "+filename, file=errFile)
		srcfile.close()
