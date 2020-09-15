#!/bin/bash

read -r -p 'Please enter the file name to commit: ' file_name

git add $file_name

git status 

read -r -p 'If you wish to continue (Y/N): ' x

if [ $x = 'N' ]; then
	exit 1
else
	read -r -p 'Please enter a commit message: ' mes
	git commit -m $mes
	git status 
	read -r -p 'If you wish to continue (Y/N): ' y
	if [ $y = 'Y' ]; then
		git push
	else
		exit 1
	fi
fi

