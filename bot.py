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

# Instanciamos el objeto del cliente de discord
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

client.run("MTAzODQ4MDQ4MTM0OTUzNzgxMg.GDIjO5.PFr1RyJfWMmLXOf6X4WL-5tbLm2UrPs9tNYskk")