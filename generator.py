import os
import sys
import xml.etree.ElementTree as ET

import reader

#todo find reason, what is THIS?!
DIR_NAME = "autodoc"


def make_folder():
    if not os.path.exists(DIR_NAME):
        os.mkdir(DIR_NAME)


def create_name(filename):
    return (filename[:-3] + ".xml")


def get_right_element(element):
    print(list(element))
    return list(element)[-1]


def find_parent(root, level):
    curelem = root
    print(level)
    if level == 0:
        return root
    else:
        for i in range(level):
            curelem = get_right_element(curelem)
        return curelem


def write_to_file(srcfile, errfile=sys.stdout):
    root = ET.Element(os.path.basename(srcfile))
    try:
        with open(srcfile, "r") as openFile:
            for line in openFile:
                resline = reader.read_line(line)
                if resline is not None:
                    #todo check wht do I need this variable?
                    elem = write_elem(find_parent(root, resline['level']), resline)
    except IOError:
        print("An error occurred while processing "+srcfile, file=errfile)
        srcfile.close()
    finally:
        tree = ET.ElementTree(root)
        tree.write(create_name(srcfile))


def write_elem(root, reslline):
    def write_class(root, resline):
        return ET.SubElement(root, resline['type'], {'name': resline['classname'], 'parent_class': resline['parent']})

    def write_function(root, resline):
        return ET.SubElement(root, resline['type'], {'name': resline['name'], 'arguments': resline['arguments']})

    def write_import(root, resline):
        return ET.SubElement(root, resline['type'], {'module': resline['module']})

    def write_comment(root, resline):
        return ET.SubElement(root, resline['type'], {'text': resline['text']})

    check = {
        'class': write_class,
        'function': write_function,
        'import': write_import,
        'comment': write_comment
    }

    return check[reslline['type']](root, reslline)