import discord
from discord.ext import commands
import aiohttp
import os

client = commands.Bot(command_prefix="?")

@client.event
async def on_ready():
    print("Chloes Ready")
    
@client.command()
async def on():
    await client.say("I am online on heroku! Wrong, and Savage")

#FUN COMMANDS:
@client.command(pass_context = True)
async def meme(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://api.reddit.com/r/me_irl/random") as r:
            author = ctx.message.author
            data = await r.json()
            embed = discord.Embed(title="Your Daily Meme",
                                  color=0x00ff00)
            embed.set_image(url = data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(icon_url=author.avatar_url, text="| Fun Commands!")

            await client.say(embed=embed)

#CONFIRGURING


#MODERARION COMMANDS:
  
    
client.run(os.environ.get('BOT_TOKEN'))
