#!/usr/bin/env python3

import os
from pathlib import Path
import subprocess


class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    INFOBLUE = '\033[94m'
    INFOCYAN = '\033[96m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class PrettyPrinter:
    
    @staticmethod
    def printOK(msg):
         print(bcolors.OKGREEN + "[OK]:" + bcolors.ENDC + " " + msg)
    
    @staticmethod
    def printWARN(msg):
         print(bcolors.WARNING + "[WARNING]:" + bcolors.ENDC + " " + msg)
    
    @staticmethod
    def printFAIL(msg):
         print(bcolors.FAIL + bcolors.BOLD + "[FAIL]:" + bcolors.ENDC + " " + msg)


def makedir(path: Path):
    try:
        os.makedirs(path)
        PrettyPrinter.printOK(f"Successfully created folder {path}")
    except FileExistsError:
        PrettyPrinter.printFAIL(f"One or more directories in '{path}' already exists")
        raise


def init_go_project(project_name):
    """ initialize a go project with name <name> in the current working directory """

    # get the current directory
    current_dir = Path(os.getcwd())

    cmd_dir = Path.joinpath(current_dir, "cmd")
    cmd_hello_dir = Path.joinpath(cmd_dir, "hello")
    cmd_hello_main = Path.joinpath(cmd_hello_dir, "main.go")

    internal_dir = Path.joinpath(current_dir, "internal")
    pkg_dir = Path(current_dir, "pkg")

    makedir(cmd_hello_dir)
    makedir(internal_dir)
    makedir(pkg_dir)

    hello_file = open(cmd_hello_main, "w")
    go_hello = """
package main

import (
    "fmt"
)

func main() {
    fmt.Println("Hello, world!")
}
"""
    hello_file.write(go_hello)
    hello_file.close()

    subprocess.getoutput(f"go mod init {project_name}")
    subprocess.getoutput("go fmt")

    # check if current directory contains cmd and pkg directories
    return

if __name__ == '__main__':
    import sys

    usage = f"{sys.argv[0]} <project-name>"

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("project_name")

    args = parser.parse_args()

    init_go_project(args.project_name)