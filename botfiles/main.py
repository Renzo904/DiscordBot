import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="!", description="Bot made it by Renzo")
token=os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready():
    print("Bot started")


@client.command(pass_context=True)
async def com(ctx, arg : str=None):
    await ctx.send("Hi!")


@client.command()
async def playing(ctx,playing : str=None):
    game = discord.Game(playing)
    await client.change_presence(activity=game)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return await ctx.send("`Comando desconocido`")
    raise error

client.run(token)

