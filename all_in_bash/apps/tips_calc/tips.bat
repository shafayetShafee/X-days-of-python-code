@echo off

rem call and mask out invalid call targets
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
   	  	echo See the help.....
   	  	echo.
   	  	goto :case-help
   	  )
   )
)

goto :eof

:case-help
	echo Runs the app 'Tips-Calculaotor' from windows cmd
	echo This app will prompt to you for Total Bill
	echo and prompt for amount of Tip Percentages
	echo and lastly, will prompt for the number of people to split the bill.
	echo.
	echo Syntax: tips.bat [help^|rich]
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


goto :eof
