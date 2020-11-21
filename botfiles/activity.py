import discord
from discord.ext import commands

class bot_activity(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def watching(self, ctx, *, video : str=None):
        video = discord.Activity(name=video, type=0)
        await self.bot.change_presence(activity=video)

    @commands.command()
    async def playing(self, ctx, *, playing : str=None):
        game = discord.Activity(name=playing, type=1)
        await self.bot.change_presence(activity=game)
    
    @commands.command()
    async def listening(self, ctx, *, listening : str=None):
        music = discord.Activity(name=listening, type=2)
        await self.bot.change_presence(activity=music)