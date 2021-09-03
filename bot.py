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

    #mensagens do geral:
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
    if message.author == client.user:
        return
    if message.channel.name == 'aed2':
        if user_message.lower()=='graph':
            await message.channel.send(f'https://github.com/victordomoto/data-structure-assignments/blob/main/graph/adjacency_matrix.c')
        elif user_message.lower()=='list':
            await message.channel.send(f'https://github.com/victordomoto/data-structure-assignments/blob/main/lists/linked_list.c')
            return 
        elif user_message.lower()=='stack':
            await message.channel.send(f'https://github.com/victordomoto/data-structure-assignments/blob/main/stack/ex1_dinamic.c')
            return
        elif user_message.lower()=='queue':
            await message.channel.send(f'https://github.com/victordomoto/data-structure-assignments/blob/main/queue/TAD-queue.c')
            return
        
        
    
client.run(TOKEN)