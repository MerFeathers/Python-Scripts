#!/usr/bin/env python3 

import shutil    #The shutil module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal. For operations on individual files, see also the os module.
import psutil    #psutil is a module that provides an interface to obtain information about a certain process and its use of the system. 

def check_disk_usage(disk):    #Check disk usage
	du = shutil.disk_usage(disk)
	free = du.free / du.total * 100
	return free

def check_cpu_usage():    #Check cpu usage
	usage = psutil.cpu_percent(1)
	return usage < 75

#checks whether disk usage in root directory is different from 0 (which is true if there is disk space)
#checks if the CPU usage is less than 75%.
#"/" is used in this context to refer to the root directory of the file system and check its disk usage.
if not check_disk_usage("/") or not check_cpu_usage():    
	print("*ERROR*")
else:
	print("Everything is OK!!!")

