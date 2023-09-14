#!/bin/bash


>oldFiles.txt    #Create the text file oldFiles.txt

files=$(grep " jane " ../data/list.txt)    #search for all lines that contain the name "jane" and save the file names into a variable

for file in $files; do
	if test -e ~/$file; then    #check if file names present in files variable are actually present in the file system
		echo ~/$file>>oldFiles.txt    #If the item within the files variable passes the test, add/append it to the file oldFiles.txt
	fi
done


	
