@echo off

if "%1" == "" (
  goto :case-base
) else (
	if "%1" == "rich" (
	  goto :case-rich
	) else (
	  	if "%1" == "help" (
	  		goto :case-help
	  	) else (
	  		echo You have used wrong Options
	  		echo see the help...
	  		echo.
	  		goto :case-help
	  	)
	)
)

goto :eof


:case-help
	echo.
	echo Run the Auction app from windows cmd
	echo This app will prompt to the user for their name and bid no
	echo At the end it gives the name of the highest bidder along with
	echo his/her bid
	echo.
	echo Syntax: auction.bat [help^|rich]
	echo Options:
	echo help 	Print this help
	echo rich	Enable the rich formatting for the app on the cli
	echo.
	goto :eof


:case-base
	python main.py
	goto :eof


:case-rich
	python main-rich.py
	goto :eof

