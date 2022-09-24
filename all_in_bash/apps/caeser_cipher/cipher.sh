#! /bin/bash

############################################################
# Help                                                     #
############################################################

Help()
{
	# display help
	echo "Runs the app 'Caeser-cipher' from bash in two mode (normal or rich formatted)"
	echo "This app will prompt you to for a text that you want to cipher or decipher"
	echo "and the shift-number in caeser-ciphering"
	echo
	echo "Syntax: bash cipher.sh [--help|--rich]"
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
		echo "Error: Invalid Option"
		;;
esac
		