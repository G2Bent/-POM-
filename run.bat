cd ./DentTest
if %ERRORLEVEL% NEQ 0 (exit 1)
:: set datetime=%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%%time:~0,2%%time:~3,2%%time:~6,2% 
:: if %ERRORLEVEL% neq 0 (exit 1)
python index.py
