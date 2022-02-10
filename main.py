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
bot = commands.Bot(command_prefix='$', case_insensitive=True)# this is to check prefix, yes prefix can be changed using file system

@bot.event
async def on_ready():
    print('We can begin the Crafting as {0.user}'.format(bot))
    #this is what is shows when the bot is online

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello!  {ctx.author}')
    #reply to the {Prefix}Hello
  
@bot.command()
async def echo(ctx, arg):
    await ctx.send(arg)
    #Reply to {Prefix}echo arguments, returns the arguments

@bot.command()
async def anime(ctx):
    await ctx.send(embed = C.EpisodeUpdate())
    #Reply to {Prefix}anime

@bot.command()
async def manga(ctx):
    await ctx.send(embed = C.MangaUpdate())
    #Replt to {Prefix}manga

import os

tk = os.environ['TOKEN']

bot.run(tk)
