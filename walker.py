__author__ = 'Duminsky Nick'
import os
import sys

import generator

#todo use errfile
def walk_through(folder, errfile=sys.stdout):
    for elem in os.listdir(folder):
        if os.path.isfile(folder+"/"+elem) & check_file(folder+"/"+elem):
            generator.write_to_file(folder+"/"+elem)
        elif os.path.isdir(folder+"/"+elem):
            walk_through(folder+"/"+elem)

#todo use errfile
#todo check do I need this function
def check_file(filename, errfile=sys.stdout):
    if filename.endswith(".py"):
        return True
    else:
        return False