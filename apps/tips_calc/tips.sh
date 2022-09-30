#! /bin/bash

############################################################
# Help                                                     #
############################################################

Help()
{
	# display help
	echo "Runs the app 'Tips-Calculaotor' from bash"
	echo "This app will prompt to you for Total Bill"
	echo "and prompt for amount of Tip Percentages"
	echo "and lastly, will prompt for the number of people to split the bill."
	echo
	echo "Syntax: bash tips.sh [--help|--rich]"
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
	
