import os.path
import sys

import generator

def checkLevel(line):
	return repr(line).split()[0].count('\\t')

def readClassDef(line):
	print(line)
	if line.find('(') != -1:
		return {'type': 'class',
				'level': checkLevel(line),
				'classname': line.split()[1].split('(')[0],
				'parent': line.split()[1].split(')')[0]}
	else:
		return {'type': 'class',
				'level': checkLevel(line),
				'classname': line.split()[1],
				'parent': 'object'}

def readFuncDef(line):
	def takeName(value):
		return value.split()[1].split('(')[0]
	def takeVals(value):
		return value.split('(')[1].split(')')[0].replace(' ','').split(',')
	#todo - change this function - it should read annotation inside takeVals()
	def takeAnnotation(value):
		return value.split('->')[1].replace(' ','')
	return {'type': 'function',
			'level': checkLevel(line),
			'name': takeName(line),
			'arguments': takeVals(line)}

def readComment(line):
	return {'type': 'comment',
			'level': checkLevel(line),
			'text': line[len(line.split()[0]):]}

def readImport(line):
	return {'type': 'import',
			'level': checkLevel(line),
			'module': line.split()[1]}

parse = {'#$': readComment,
   	     'class': readClassDef,
       	 'def': readFuncDef,
       	 'import': readImport}

def readFile(srcFile, errFile=sys.stdout):
	try:
		with open(srcfile, "r") as curFile:
			for line in curFile:
				readLine(line)
	except IOError as err:
		print("An error occured while processing "+srcFile+ " " +str(err.errno), file=errFile)

def readLine(line):
	try:
		return parse[line.split()[0]](line)
	#not a keyword
	except KeyError:
		pass
	#empty string
	except IndexError:
		pass