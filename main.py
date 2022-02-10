from distutils.debug import DEBUG
import discord
import commands as C
from discord.ext import commands

'''
New Base!
@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)
'''
bot = commands.Bot(command_prefix='$')

#client = discord.Client()

@bot.event
async def on_ready():
    print('We can begin the Crafting as {0.user}'.format(bot))

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello!  {ctx.author}')
  
@bot.command()
async def echo(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def anime(ctx):
    await ctx.send(embed = C.EpisodeUpdate())

@bot.command()
async def manga(ctx):
    await ctx.send(embed = C.MangaUpdate())

import os

tk = os.environ['TOKEN']

bot.run(tk)
