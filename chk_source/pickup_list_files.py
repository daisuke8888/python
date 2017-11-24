#! python3

import os
import re
import sys

def list_ext(extension, dirname='.'):
    list_files = []
    regex = r'.*\.' + extension + r'$'
    for foldername, subfolders, filenames in os.walk(dirname):
        for filename in filenames:
            file_re = re.compile(regex)
            justfile = file_re.search(filename)
            if(None != justfile):
                list_files.append(os.path.join(foldername, justfile.group()))
    return list_files

def list_cpp(dirCpp='.'):
    return list_ext('cpp', dirname=dirCpp)

def list_h(dirHeader='.'):
    return list_ext('h', dirname=dirHeader)

def list_cs(dirCs='.'):
    return list_ext('cp', dirname=dirCs)

def list_log(dirLog='.'):
    return list_ext('log', dirname=dirLog)

if(__name__ == "__main__"):
    argvs = sys.argv
    argc = len(argvs)

    if(2 == argc):
        print(list_cpp(argvs[1]))
        print(list_h(argvs[1]))
        print(list_cs(argvs[1]))
        print(list_log(argvs[1]))
    else:
        print(list_cpp())
        print(list_h())
        print(list_cs())
        print(list_log())


