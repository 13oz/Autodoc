import sys


def check_level(line):
    return repr(line).split()[0].count('\\t')


def read_class_def(line):
    print(line)
    if line.find('(') != -1:
        return {'type': 'class',
                'level': check_level(line),
                'classname': line.split()[1].split('(')[0],
                'parent': line.split()[1].split(')')[0]}
    else:
        return {'type': 'class',
                'level': check_level(line),
                'classname': line.split()[1],
                'parent': 'object'}


def read_func_def(line):
    def take_name(value):
        return value.split()[1].split('(')[0]

    def take_vals(value):
        return value.split('(')[1].split(')')[0].replace(' ','').split(',')

    #todo - change this function - it should read annotation inside take_vals()
    #def take_annotation(value):
    #    return value.split('->')[1].replace(' ','')

    return {'type': 'function',
            'level': check_level(line),
            'name': take_name(line),
            'arguments': take_vals(line)}


def read_comment(line):
    return {'type': 'comment',
            'level': check_level(line),
            'text': line[len(line.split()[0]):]}


def read_import(line):
    return {'type': 'import',
            'level': check_level(line),
            'module': line.split()[1]}

parse = {'#$': read_comment,
         'class': read_class_def,
         'def': read_func_def,
         'import': read_import}


def read_file(srcfile, errfile=sys.stdout):
    try:
        with open(srcfile, "r") as curFile:
            for line in curFile:
                read_line(line)
    except IOError as err:
        print("An error occurred while processing "+srcfile+ " " +str(err.errno), file=errfile)


def read_line(line):
    try:
        return parse[line.split()[0]](line)
    #not a keyword
    except KeyError:
        pass
    #empty string
    except IndexError:
        pass