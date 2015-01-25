#!/usr/bin/python

import os
import sys


def convert_grep_file_arg(grep_file_arg) :
    arg_len = len(grep_file_arg)
    
    if grep_file_arg[arg_len-1] != ':' :
        return grep_file_arg
    
    i = arg_len - 2
    while i >= 0 :
        if grep_file_arg[i] == ':' :
            break
        i -= 1
    if i == -1 :
        return grep_file_arg

    try:
        line = int(grep_file_arg[i+1: arg_len-1])
    except ValueError :
        return grep_file_arg
    else:
        return grep_file_arg[0: i] + " +" + str(line)


def get_origin_command(argv) :
    result = ""
    for arg in argv :
        result += arg + " "
    return result


if __name__  == "__main__" :
    if len(sys.argv) == 2 :
        os.system("vim " + convert_grep_file_arg(sys.argv[1]))
    else:
        os.system("vim " + get_origin_command(sys.argv[1:]))
