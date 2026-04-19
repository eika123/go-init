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


class PrintLogger:
    
    def logOK(self, msg):
         print(bcolors.OKGREEN + "[OK]:" + bcolors.ENDC + " " + msg)
    
    def logWARN(self, msg):
         print(bcolors.WARNING + "[WARNING]:" + bcolors.ENDC + " " + msg)
    
    def logFAIL(self, msg):
         print(bcolors.FAIL + bcolors.BOLD + "[FAIL]:" + bcolors.ENDC + " " + msg)
    

def init_go_project(project_name):
    """ initialize a go project with name <name> in the current working directory """

    logger = PrintLogger()

    # get the current directory
    current_dir = Path(os.getcwd())

    cmd_dir = Path.joinpath(current_dir, "cmd")
    cmd_hello_dir = Path.joinpath(cmd_dir, "hello")
    cmd_hello_main = Path.joinpath(cmd_hello_dir, "main.go")


    internal_dir = Path.joinpath(current_dir, "internal")
    pkg_dir = Path(current_dir, "pkg")


    try:
        os.makedirs(cmd_hello_dir)
        logger.logOK(f"Successfully created folder {cmd_hello_dir}")
    except FileExistsError:
            logger.logFAIL(f"One or more directories in '{cmd_hello_dir}' already exists")
            raise

    try:
        os.mkdir(internal_dir)
        logger.logOK(f"Successfully created folder {internal_dir}")
    except FileExistsError:
            logger.logFAIL(f"One or more directories in '{internal_dir}' already exists")
            raise
    
    try:
        os.mkdir(pkg_dir)
        logger.logOK(f"Successfully created folder {pkg_dir}")
    except FileExistsError:
            logger.logFAIL(f"One or more directories in '{pkg_dir}' already exists")


    hello_file = open(cmd_hello_main, "w")
    go_hello = """
package main

import (
    "fmt"

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
    init_go_project("test")