import discord
from discord.ext import commands

TOKEN = "NTAzMzg2NTU4OTc2NjIyNTkz.Dq1uzw.c5iE5nKmzK1d784QQ7loea0SWac"

client = commands.Bot(command_prefix="?")

@client.event
async def on_ready():
    print("Chloes Ready")

client.run(TOKEN)




