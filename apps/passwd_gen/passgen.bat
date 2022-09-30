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
	echo Runs the app 'Password Generator' from windows cmd
	echo This app will prompt to you for three things
	echo 		1. How many small case letter to use in Password?
	echo 		2. How many numbers to use in Password?
	echo 		3. How many punctuations to use in Password?
	echo
	echo Syntax: passgen.bat [help^|rich]
	echo Options:
	echo help Print this help
	echo rich	Enable the rich formatting for the app on the cli
	echo
	goto :eof

:case-base
	python main.py
	goto :eof

:case-rich
	python main-rich.py
	goto :eof


goto :eof
