#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "kamela williamson"
# got clarifiaction on parts of assessment from Jalon and DeQuan
# https://automatetheboringstuff.com/chapter8/
# https://docs.python.org/3/library/os.path.html
# https://www.tutorialspoint.com/python/os_listdir.htm
# https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings
# https://docs.python.org/3/library/subprocess.html
# https://www.youtube.com/watch?v=2Fp1N6dof0Y&feature=youtu.be
# https://docs.python.org/3/tutorial/stdlib.html

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    # returns list of absolute paths of special files in given directory
    # your code here
    d_files = os.listdir(dirname)
    special_files = []
    # print
    for file in d_files:
        s_file = re.search(r'__\w+__', file)
        if s_file:
            special_files.append(os.path.abspath(os.path.join(dirname, file)))
    return special_files


def copy_to(path_list, dest_dir):
    """copy files into the directory from the paths"""
    # your code here
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
    for path in path_list:
        dest_path = os.path.join(dest_dir, os.path.basename(path))
        print('copy_to = {} dest_path = {} '.format(path, dest_path))
        shutil.copy(path, dest_path)


def zip_to(path_list, dest_zip):
    """zip files up into a zipfile """
    # your code here
    cmd = ['zip', '-j', dest_zip]
    cmd.extend(path_list)
    print('Command about to be executed: {}'.format(cmd))
    subprocess.call(cmd)


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument('from_dir', help='origin dir for special files')
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).
    # Your code here: Invoke (call) your functions
    if not ns:
        parser.print_usage()
        sys.exit(1)

    todir = ns.todir
    tozip = ns.tozip
    from_dir = ns.from_dir
    special_files = get_special_paths(from_dir)
    if todir:
        copy_to(special_files, todir)
    elif tozip:
        zip_to(special_files, tozip)
    else:
        print('\n'.join(special_files))


if __name__ == "__main__":
    main(sys.argv[1:])
