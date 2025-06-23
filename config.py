import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20475158"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "89a119fa2c6408e3037949b8cc815233")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://chanpreet161616:HNGaeiIDpbJatyEt@cluster0.fnyma4q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
