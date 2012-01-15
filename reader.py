import generator
import os.path

TRAILER = """\n\n\nThis documentation file was generated with help of AutoDoc software by Nick Duminsky aka 13oz ,
if ypu want to send bugreport, tell me, what you want to see in next version, or just give me advice, 
mailto: duminsky.nick@gmail.com"""

def addIndent(line):
	level=0
	res = ""
	while level < (repr(line).split()[0].count('\\'))/2:
		res += '\t'
		level += 1
	return res

def readClassDef(line):
	if line.find('(') != -1:
		return addIndent(line) + "Class {0} extends {1}".format(line.split()[1].split('(')[0], line.split('(')[1].split(')')[0])
	else:
		return addIndent(line) + "Class {0}".format(line.split()[1])

def readFuncDef(line):
	res = ""
	def takeDefVals(values):
		for val in values:
			if val == "self":
				yield addIndent(line) + "{0}{1} - is a link to self class object\n".format(addIndent(line), val)
			elif val.find("=") != -1:
				yield addIndent(line) + "{0}{1} with default value {2}\n".format(addIndent(line),val.split('=')[0],val.split('=')[1])
			else:
				yield addIndent(line) + "{0}{1} without defult value\n".format(addIndent(line),val)
	def takeAnnotation(values):
		for val in values:
			if val =="self":
				yield addIndent(line) + "{0}{1} - is a link to self class object\n".format(addIndent(line), val)
			else:
				yield addIndent(line) + "{0}{1} as {2}\n".format(addIndent(line), val.split(':')[0], val.split(':')[1])
	if line.find("->") != -1:
		res = addIndent(line) + "Function {0} takes:\n".format(line.split()[1].split('(')[0])
		for val in takeAnnotation(line.split('(')[1].split(')')[0].split(',')):
			res += addIndent(line) + val
		return res
	else:
		res = addIndent(line) + "Function {0} takes:\n".format(line.split()[1].split('(')[0])
		for var in takeDefVals(line.split('(')[1].split(')')[0].split(',')):
			res += addIndent(line) + var
		return res

def readComment(line):
	return addIndent(line) + line[len(line.split()[0]):]

def readImport(line):
	return addIndent(line) + line.split()[0]

parse = {'#$': readComment,
   	     'class': readClassDef,
       	 'def': readFuncDef,
       	 'import': readImport}

def readFile(srcFile):
	result = 'Module '+os.path.basename(srcFile)+'\n\n'
	try:
		for line in open(srcFile, "r"):
			res = readLine(line)
			if res == -1: 
				pass
			else:
				result += res + '\n'
	except IOError:
		print("An error occured while processing "+srcFile, file=sys.stderr)
	finally:
		result += TRAILER
		generator.writeToFile((generator.formFileName(srcFile)), result)
	
def readLine(line):
	try:
		return parse[line.split()[0]](line)
	#not a keyword
	except KeyError:
		return -1
	#empty string
	except IndexError:
		return -1

readFile("G:/Dropbox/Python/Source-struct/strider.py")