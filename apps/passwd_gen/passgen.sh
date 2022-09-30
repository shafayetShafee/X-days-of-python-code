#! /bin/bash

############################################################
# Help                                                     #
############################################################

Help()
{
	# display help
	echo "Runs the app 'Password Generator' from bash"
	echo "This app will prompt to you for three things"
	echo "		1. How many small case letter to use in Password?"
	echo "		2. How many numbers to use in Password?"
	echo "		3. How many punctuations to use in Password?"
	echo
	echo "Syntax: bash passgen.sh [--help|--rich]"
	echo "Options:"
	echo "--help 	Print this help"
	echo "--rich	Enable the rich formatting for the app on the cli"
	echo
}


############################################################
############################################################
# Main program                                             #
############################################################
############################################################


case $1 in
	"--help")
		Help
		;;
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
	
