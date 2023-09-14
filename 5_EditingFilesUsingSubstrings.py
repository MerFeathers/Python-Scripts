#!/usr/bin/env python3

import sys    #The sys (System-specific parameters and functions) module provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.
import subprocess    #The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and get their return codes.

old_Files = sys.argv[1]    #Since oldFiles.txt is passed as a command line argument, it's stored in the variable sys.argv[1]

with open(old_Files, mode='r',encoding='UTF-8') as f:
	for line in f.readlines():
		old_name = line.strip()
		new_name = old_name.replace("jane", "jdoe")    #replace old name with new name in new_name
		command = ["mv", old_name, new_name]    #to rename the files in the file system
		subprocess.run(command)    #invoke a subprocess by calling run() function. This function takes arguments used to launch the process. These arguments may be a list or a string
		"""Use the mv command to rename the files in the file system. This command moves a file or directory. It takes in source file/directory and destination file/directory as parameters. We'll move the file with old name to the same directory but with a new name.
		You should pass a list consisting of the mv command, followed by the variable storing the old name and new name respectively to the run() function within the subprocess module."""
f.close()
