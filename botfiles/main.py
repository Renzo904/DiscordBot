import discord
import os
from discord.ext import commands
from discord.ext import tasks
from activity import bot_activity



intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!", intents = intents, description = "Bot made it by Renzo")
token = os.getenv("DISCORD_BOT_TOKEN")

@bot.event
async def on_ready():
    print("Bot started")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="general")
    await channel.send(f"Bienvenido al servidor {member.mention}!!")
    print(f"Se ha unido el miembro {member.name}")
    

@bot.command(pass_context=True)
async def com(ctx, arg : str=None):
    await ctx.send("Hi!")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return await ctx.send("`Comando desconocido`")
    raise error

bot.add_cog(bot_activity(bot))
bot.run(token)

