
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        

        if self.user.mentioned_in(message):
            if "hola" in message.content:
                print(message.content)
                await message.channel.send("Pa ti mi cola")