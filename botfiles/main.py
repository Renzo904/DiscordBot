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
    print(f"Se ha unido el miembro {member.name}")

@bot.event
async def on_message(msg):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',msg.content.lower())
    if urls and not msg.author.top_role.permissions.manage_messages:
        await msg.delete()
        await msg.channel.send("No puedes enviar enlaces en este servidor")

@bot.event
async def on_message_edit(bf,af):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',af.content.lower())
    if urls and not af.author.top_role.permissions.manage_messages:
        await af.delete()
        await af.channel.send("No puedes enviar enlaces en este servidor")

@bot.command(pass_context=True)
async def prefix(ctx, prefix : str=None):
    bot.command_prefix=prefix

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return await ctx.send(f"`Comando desconocido\nUse {bot.command_prefix}help para ver los comandos`")
    raise error

bot.add_cog(bot_activity(bot))
bot.run(TOKEN)

