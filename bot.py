#bot.py
import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(f'{client.user} has connected to the guild:\n'
    f'{guild.name}(id: {guild.id})')

    """ This prints the members of the guild
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    """

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!kill':
        quote = 'It\'s the first kill? For sure Connor'
        await message.channel.send(quote)
    elif message.content == '!josh':
        quote = 'That\'s that dude that only votes Connor right?'
        await message.channel.send(quote)
    elif message.content == '!bestwaifu':
        quote = '❤️❤️❤️ Rem ❤️❤️❤️'
        await message.channel.send(quote)
        await message.channel.send(file=discord.File('thumb-1920-710132.png'))
    elif message.content == '!waifu':
        quote = ['Asuna from SAO', 'Mio Akiyama from K-On!', 'Makise Kurisu from Steins;Gate',
                'Saber from Fate', 'Emilia from Re Zero', 'Rukia Kuchiki from Bleach',
                'Akame from Akame Ga Kill']
        response = (f'{message.author}' + ', your waifu is ' + random.choice(quote))
        await message.channel.send(response)
    elif message.content == '!help':
        quote = 'Random Commands:\n!kill = Prints off a funny meme about killing Connor\n'
        quote = quote + '!josh = Prints off a meme about Josh\'s play style\n!bestwaifu = Tells you who the best waifu is\n'
        quote = quote + '!waifu = gives you a random waifu'
        await message.channel.send(quote)

client.run(TOKEN)
