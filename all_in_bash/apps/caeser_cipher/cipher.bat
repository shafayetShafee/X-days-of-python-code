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
	echo Runs the app 'Caeser-cipher' from windows cmd in two mode (normal or rich formatted)
	echo This app will prompt you to for a text that you want to cipher or decipher
	echo and the shift-number in caeser-ciphering
	echo.
	echo Syntax: cipher.bat [help^|rich]
	echo Options:
	echo help Print this help
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
