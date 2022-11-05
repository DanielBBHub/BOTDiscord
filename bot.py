""" Codigo desarrollado para implementar un bot con funcionalidad de calendario (por ahora)
-Daniel (dabebel)

"""

# bot.py
import os

import discord
from cliente import MyClient
from dotenv import load_dotenv

# Cargamos el token de acceso del bot desde el archivo token.env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN = TOKEN[1:-1]
print(TOKEN)

intents = discord.Intents.default()
intents.message_content = True

# Instanciamos el objeto del cliente de discord 
client = MyClient(intents=intents)

client.run(TOKEN)
