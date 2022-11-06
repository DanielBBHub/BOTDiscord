
import discord
import calendario as c

# Libreria de la que extraemos funciones de expresiones regulares
import re

class MyClient(discord.Client):
    
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        self.calendario = c.Calendario()
        self.REGEX = "^\$([a-z]*) !([0-9]*-[0-9]*-[0-9]*) ([A-Z]*[a-z]+) ([A-Z]*[a-z]+)"
        
       
        
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        
        match = re.match(self.REGEX, message.content)
        if match.groups()[0] == "examen":
            self.calendario.anyadir_examen(match.groups()[1],match.groups()[2],match.groups()[3])
            print("Comando: {0} \nArgumentos: {1}".format(match.groups()[0], match.groups()[1:]))

        if self.user.mentioned_in(message):
            if "hola" in message.content:
                await message.channel.send("Pa ti mi cola")


            

            
                    