import os.path
import sys

import generator

parse = {'#$': readComment,
   	     'class': readClassDef,
       	 'def': readFuncDef,
       	 'import': readImport}

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
	return checkLevel(line), line[len(line.split()[0]):]

def readImport(line):
	return checkLevel(line), line.split()[0]

def readFile(srcFile, errFile=sys.stdout):
	try:
		for line in open(srcFile, "r"):
			yield readLine(linel)
	except IOError as err:
		print("An error occured while processing "+srcFile+ " " +err.errno, file=errFile)
	
def readLine(line):
	try:
		return parse[line.split()[0]](line)
	#not a keyword
	except KeyError:
		pass
	#empty string
	except IndexError:
		pass