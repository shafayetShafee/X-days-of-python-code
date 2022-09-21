#! /bin/bash

case $1 in
	"--rich")
		python main-rich.py
		;;
	"")
		python main.py
		;;
	*)
		echo "Invalid Option"
		;;
esac
	
