import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7574475855:AAHvO7iVsRXAnvWb-bP9kd1DvbOK_-NEy_o")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22451323"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "9edcc32d1848771360efa9379868d352")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://heroku:heroku@cluster0.wamwxpr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
