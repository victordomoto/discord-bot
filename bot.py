import discord
import random
import os


from discord import user
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
@client.event
async def on_ready():
    print('{0.user}'.format(client))



@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    #mensagens no geral:
    if message.author == client.user:
        return
    if message.channel.name == 'geral':
        if user_message.lower()=='hello':
            await message.channel.send(f'hello {username}!')
        elif user_message.lower()=='bye':
            await message.channel.send(f'see you latter {username}!')
            return 
        elif user_message.lower()=='!random':
            response = f'{random.randrange(1000000)}'
            await message.channel.send(response)
            return
    #mensagens em aed2:

    
client.run(TOKEN)