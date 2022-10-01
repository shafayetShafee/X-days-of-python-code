#! /bin/bash

############################################################
# Help                                                     #
############################################################

Help() 
{
	# display help
	echo "Run the Auction app from bash"
	echo "This app will prompt to the user for their name and bid no"
	echo "At the end it gives the name of the highest bidder along with"
	echo "his/her bid"
	echo
	echo "Syntax: bash auction.sh [--help|--rich]"
	echo "Options:"
	echo "--help 	Print this help"
	echo "--rich	Enable the rich formatting for the app on the cli"
	echo
}


############################################################
# Main program                                             #
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
		echo
		echo "Invalid Option"
		echo "See help for correct option"
		echo
		Help
		;;
esac