import discord
from discord import channel
from discord.ext import commands
import os


client = commands.Bot(command_prefix="!")
token=os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready():
    print("Bot started")


@client.command()
async def welcome(ctx):
    await ctx.send("holis") 


client.run(token)

