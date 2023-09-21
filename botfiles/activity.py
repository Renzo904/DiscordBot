import discord
from discord.ext import commands
import logging

class bot_activity(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def watching(self, ctx, *, video : str=None):
        video = discord.Activity(name=video, type=0)
        
        self.bot.logger.info(f"Changing activity to watching {video}")
        await self.bot.change_presence(activity=video)

    @commands.command()
    async def playing(self, ctx, *, playing : str=None):
        game = discord.Activity(name=playing, type=1)
        self.bot.logger.info(f"Changing activity to playing {playing}")
        await self.bot.change_presence(activity=game)
    
    @commands.command()
    async def listening(self, ctx, *, listening : str=None):
        music = discord.Activity(name=listening, type=2)
        self.bot.logger.info(f"Changing activity to listening {listening}")
        await self.bot.change_presence(activity=music)