#! /bin/bash

############################################################
# Help                                                     #
############################################################

Help()
{
	# display help
	echo "Run the app 'bandname-generator' from bash"
	echo "This app will prompt to you for your city name and pet name"
	echo "and then combine those name to create a band name for you."
	echo
	echo "Syntax: bash bandname.sh [--help|--rich]"
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
	
