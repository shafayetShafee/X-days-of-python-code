#! /bin/bash

############################################################
# Help                                                     #
############################################################

Help()
{
	# display help
	echo "Run the game 'Hangman' from bash"
	echo
	echo "Syntax: bash hangman.sh [--help|--rich]"
	echo "Options:"
	echo "--help 	Print this help"
	echo "--rich	Enable the rich formatting for the game on the cli"
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
	
