#! python3

import os
import re
import sys

def list_cpp(dirtest='.'):
    list_file_cpp = []
    for foldername, subfolders, filenames in os.walk(dirtest):
        for filename in filenames:
            file_re = re.compile(r'.*\.cpp$')
            file_cpp = file_re.search(filename)
            if(None != file_cpp):
                list_file_cpp.append(os.path.join(foldername, file_cpp.group()))
    return list_file_cpp

def list_h(dirtest='.'):
    list_file_h = []
    for foldername, subfolders, filenames in os.walk(dirtest):
        for filename in filenames:
            file_re = re.compile(r'.*\.h$')
            file_h = file_re.search(filename)
            if(None != file_h):
                list_file_h.append(os.path.join(foldername, file_h.group()))
    return list_file_h

def list_cs(dirtest='.'):
    list_file_cs = []
    for foldername, subfolders, filenames in os.walk(dirtest):
        for filename in filenames:
            file_re = re.compile(r'.*\.cs$')
            file_cs = file_re.search(filename)
            if(None != file_cs):
                list_file_cs.append(os.path.join(foldername, file_cs.group()))
    return list_file_cs

if(__name__ == "__main__"):
    argvs = sys.argv
    argc = len(argvs)

    if(2 == argc):
        print(list_cpp(argvs[1]))
        print(list_h(argvs[1]))
        print(list_cs(argvs[1]))
    else:
        print(list_cpp())
        print(list_h())
        print(list_cs())


