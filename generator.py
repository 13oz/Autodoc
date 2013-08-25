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
	return (filename[:-3] + ".xml")

def getRightElement(element):
	print(list(element))
	return list(element)[-1]

def findParent(root, level):
	curElem = root
	print(level)
	if level == 0:
		return root
	else:
		for i in range(level):
			curElem = getRightElement(curElem)
		return curElem

def writeToFile(srcfile, errFile=sys.stdout):
	root = ET.Element(os.path.basename(srcfile)) 
	try:
		with open(srcfile, "r") as openFile:
			for line in openFile:
				resLine = reader.readLine(line)
				if resLine != None:
					elem = writeElem(findParent(root, resLine['level']), resLine)
	except IOError:
		print("An error occured while processing "+filename, file=errFile)
		srcfile.close()
	finally:
		tree = ET.ElementTree(root)
		tree.write(createName(srcfile))

def writeElem(root, resLine):
	def writeClass(root, resLine):
		return ET.SubElement(root, resLine['classname'], {'parent class': resLine['parent']})

	def writeFunction(root, resLine):
		return ET.SubElement(root, resLine['name'], {'arguments': resLine['arguments']})

	def writeImport(root, resLine):
		return ET.SubElement(root, resLine['type'], {'module': resLine['module']})

	def writeComment(root, resLine):
		return ET.SubElement(root, resLine['type'], {'text': resLine['text']})

	check = {
	'class': writeClass,
	'function': writeFunction,
	'import': writeImport,
	'comment': writeComment
	}

	return check[resLine['type']](root, resLine)