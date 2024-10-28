This is sample project to evalute jenkins CI/CI pipeline.

localhost URL creation please follow steps here: https://dashboard.ngrok.com/get-started/setup/windows
OR follow below steps for windows

Download ngrok
extract to folder
navigate to the extracted folder and open cmd
authenticate ngrok using cmd command "ngrok config add-authtoken 2nxNICzYWVTINPmP7EzCBbs3pfh_2PgbA3Qzaz1AmFmCNFbLX" 
Note: If you see any issue for authentication then please navigate here https://dashboard.ngrok.com/get-started/setup/windows to confirm access token 
convert http:\\localhost.8080 using cmd "ngrok htttp 8080"
If all went well then new jenkins address will be displaying on the cmd
Note: This address is temp until ngrok cmd window is open, next time you will get another address since we are using free plan.

For --alluredir error please use "python -m pip install pytest allure-python-commons allure-pytest" to recfity errors related to allure

