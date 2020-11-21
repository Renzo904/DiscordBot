import discord
import os
from discord.ext import commands
from discord.ext import tasks
from activity import bot_activity
import re

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents = intents, description = "Bot made it by Renzo")


@bot.event
async def on_ready():
    print("Bot started")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="general")
    await channel.send(f"Bienvenido al servidor {member.mention}!!")
    print(f"Se ha unido el miembro {member.name}  prefix:{bot.command_prefix}")

@bot.command(pass_context=True)
async def prefix(ctx, prefix : str=None):
    bot.command_prefix=prefix
    await ctx.channel.send(f"Prefix cambiado a {bot.command_prefix}")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return await ctx.send(f"`Comando desconocido\nUse {bot.command_prefix}help para ver los comandos`")
    raise error

bot.add_cog(bot_activity(bot))
bot.run(TOKEN)

