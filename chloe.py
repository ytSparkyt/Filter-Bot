import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="?")

@client.event
async def on_ready():
    print("Chloes Ready")
    
@client.command()
async def on():
    await client.say("I am online on heroku! Wrong, and Savage")

client.run(os.environ.get('BOT_TOKEN'))
