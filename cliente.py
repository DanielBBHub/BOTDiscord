
import discord
import calendario as c
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        c.Calendario()
        
    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        

        if self.user.mentioned_in(message):
            if "hola" in message.content:
                print(message.content)
                await message.channel.send("Pa ti mi cola")

            if "$" in message.content:
                mensaje = message.content.split("$")
                print(f"Mensaje recibido: {mensaje} ")
                if "examen" in mensaje[1]:
                    print(f"Comando recogido: {mensaje[1]} ")
                    args = mensaje[1].split("!")
                    args = args[1].split(" ")
                    print(f"Examen recogido: {args}")
                    