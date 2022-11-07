import discord
import calendario as c

# Libreria de la que extraemos funciones de expresiones regulares
import re

from discord.utils import get

class MyClient(discord.Client):
    
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        self.calendario = c.Calendario()
        self.REGEX = "^\$([a-z]*) !([0-9]*-[0-9]*-[0-9]*) ([A-Z]*[a-z]+) ([A-Z]*[a-z]+)"
        self.recoger_miembros()
        for guilds in self.guilds:
            print(guilds)
       
        
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        
        
        match = re.match(self.REGEX, message.content)
        if match:
            if match.groups()[0] == "examen":
                self.calendario.anyadir_examen(match.groups()[1],match.groups()[2],match.groups()[3])
                print("Comando: {0} \nArgumentos: {1}".format(match.groups()[0], match.groups()[1:]))
            #elif match.group()[0] == "miembro":


        if self.user.mentioned_in(message):
            if "hola" in message.content:
                await message.channel.send("Pa ti mi cola")


            
    def recoger_nombre(self, miembros):
        nombres = dict()
        nombres.setdefault(miembros.id,miembros.name)
        return nombres

    def recoger_miembros(self):
        
        for miembro in self.get_all_members():
            print(f"Miembro recogido: {miembro.id}")
            print(f"Miembro recogido: {self.get_user(miembro.id)}")
            