from time import sleep
import discord
import commands as C
from discord.ext import commands
import asyncio
import helper_commands as hp

Yeah = ["y","ye","yes","Okay","k","kay","true","t","true",1,'enable', 'on']
Nah = ["n","no","f","false",0,'disable', 'off']

bot = commands.Bot(command_prefix='$', case_insensitive=True)
#This is to check prefix, yes prefix can be changed using file system

@bot.event
async def on_ready():
    print('We can begin the Crafting as {0.user}'.format(bot))
    #this is what is shows when the bot is online

    bot.DelMsg = True
'''
@bot.event#ping reply
async def on_message(message):
  if message.author.bot == False and bot.user.mentioned_in(message) and len(message.content) == len(bot.user.mention)+1:
    await message.channel.send(f'Hello! I am the {bot.user.mention}!\nMy Prefix is $')
  await bot.process_commands(message)
'''
@bot.command()
async def prefix(ctx):
  if bot.DelMsg:await ctx.message.delete()
  await ctx.send('$')

@bot.command(name='hello',aliases=['hey','hola','hi'])
async def hello(ctx):
  if bot.DelMsg:await ctx.message.delete()
  await ctx.send(f'Hello!  {ctx.author.mention}')
  #reply to the {Prefix}Hello

@bot.command()
async def echo(ctx, *, arg):
  if bot.DelMsg:await ctx.message.delete()
  await ctx.send(arg)

@bot.command(name='anime',aliases=['A'])
async def anime(ctx):
  if bot.DelMsg:await ctx.message.delete()
  await ctx.send(embed = C.EpisodeUpdate())

@bot.command(name='manga',aliases=['M'])
async def manga(ctx):
  if bot.DelMsg:await ctx.message.delete()
  await ctx.send(embed = C.MangaUpdate())

@bot.command(name = 'autodelmessage',aliases = ['ADM'] )
async def autodelmessage(ctx,arg):
  arg = arg.lower()
  msg = "Invaild Input!\n`$autodelmessage <True/False>`"
  #temp = bot.DelMsg
  if arg in Yeah:
    bot.DelMsg = True
    msg = "Auto Delete Command Message is On"
  elif arg in Nah:
    bot.DelMsg = False
    msg = "Auto Delete Command Message is Off"

  if bot.DelMsg == True:
    await ctx.message.delete()
  #bot.DelMsg = temp
  await ctx.send(msg)

import os

tk = os.environ['TOKEN']

bot.run(tk)
