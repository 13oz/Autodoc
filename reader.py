import os.path
import sys

import generator

parse = {'#$': readComment,
   	     'class': readClassDef,
       	 'def': readFuncDef,
       	 'import': readImport}

TRAILER = """\n\n\nThis documentation file was generated with help of AutoDoc software by Nick Duminsky aka 13oz ,
if ypu want to send bugreport, tell me, what you want to see in next version, or just give me advice, 
mailto: duminsky.nick@gmail.com"""

#deprecated
def addIndent(line):
	level=0
	while level < (repr(line).split()[0].count('\\t'))/2:
		level += 1
	return "\t"*level

def checkLevel(line):
	return repr(line).split()[0].count('\\t')

def readClassDef(line):
	if line.find('(') != -1:
		#(level, classname, parent class name)
		return checkLevel(line), line.split()[1].split('(')[0], line.split()[1].split(')')[0]
	else:
		#(level, classname)
		return checkLevel(line), line.split()[1]

def readFuncDef(line):
	def takeName(value):
		return value.split()[1].split('(')[0]
	def takeVals(value):
		return value.split('(')[1].split(')')[0].replace(' ','').split[',']
	def takeAnnotation(value):
		return value.split('->')[1].replace(' ','')
	#(level, 'funcname', ['arg1', 'arg2'], 'return type')
	return checkLevel(line), takeName(line), takeVals(line), takeAnnotation(line)
			

def readComment(line):
	return addIndent(line) + line[len(line.split()[0]):]

def readImport(line):
	return addIndent(line) + line.split()[0]

def readFile(srcFile, errFile):
	result = 'Module '+os.path.basename(srcFile)+'\n\n'
	try:
		for line in open(srcFile, "r"):
			res = readLine(line)
			if res == -1: 
				pass
			else:
				result += res + '\n'
	except IOError as err:
		print("An error occured while processing "+srcFile+ " " +err.errno, file=errFile)
	finally:
		result += TRAILER
		generator.writeToFile((generator.formFileName(srcFile)), result, errFile)
	
def readLine(line):
	try:
		return parse[line.split()[0]](line)
	#not a keyword
	except KeyError:
		return -1
	#empty string
	except IndexError:
		return -1