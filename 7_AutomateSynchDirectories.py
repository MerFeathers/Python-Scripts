#!/usr/bin/env python3

import multiprocessing    #This module provides support for concurrent execution of code using processes (parallelism)
from multiprocessing import Pool    #The Pool class is used to create a pool of worker processes, allowing you to parallelize tasks by distributing them among multiple CPU cores or processors.
import subprocess    #This module is used to spawn new processes, connect to their input/output/error pipes, and obtain return codes from them
import os    #This module provides functions for interacting with the operating system, such as file and directory manipulation, environment variables, and process management


def sync_directory(args):
    src, dest = args
    subprocess.call(["rsync", "-arq", src, dest])    #---------------sync your data recursively from the source path to the destination path.

if __name__ == "__main__":
    home_dir = os.path.expanduser("~")    #--------------------------------------------------------------determine the user's home directory
    src = home_dir + "/data/prod/"    #------------------------------------------------------------------determine src directory
    dest = home_dir + "/data/prod_backup/"    #------------------------------------------------------------------determine dest directory

    directories_to_sync = [(src, dest)]

    with Pool(processes=multiprocessing.cpu_count()) as pool:    #create a pool of worker processes. The number of processes is set to the number of CPU cores available
        pool.map(sync_directory, directories_to_sync)    #pool.map function is used to concurrently execute the sync_directory function for each tuple in the directories_to_sync list. The synchronization of directories happens in parallel, leveraging multiple CPU cores for faster execution


