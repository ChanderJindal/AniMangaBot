import discord
import commands as C
from discord.ext import commands
import asyncio

'''
New Base!
@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)
'''

Anime_Channel = 736777686596190208
Manga_Channel = 736776933014110338
test_channel = 829814770453839895
Yeah = ["y","ye","yes","Okay","k","kay","true","t","true",True,1,'enable', 'on']
Nah = ["n","no","f","false",False,0,'disable', 'off']

bot = commands.Bot(command_prefix='$', case_insensitive=True)
#This is to check prefix, yes prefix can be changed using file system


'''
async def tester():
  while True:

    await asyncio.sleep(30)

    channel = bot.get_channel(test_channel)
    await channel.send("This command is here.")
    Val = C.Anime_Update_Check()#checks anime updates, it has all the info there
    if Val != False:#if anything but False then pass
      await channel.send(embed=Val)

    Val = C.Manga_Update_Check()#same as above but for manga
    if Val != False:
      await channel.send(embed=Val)
    await channel.send("This command is not here.")
'''

async def AutoUpdates(AVal,MVal,flag = True):
  while flag == True:
    Val = C.EpisodeUpdate() #New way to check, get the regular message
    EmbedDict = Val.to_dict()
    if EmbedDict["title"] != "Error!": #if not Error, i.e. the function is working
      Cval = C.GetAnimeEpisodeNumber(EmbedDict["description"])
      if Cval > AVal:
        AVal = Cval
        channel = bot.get_channel(Anime_Channel)
        await channel.send(embed=Val)

    Val = C.MangaUpdate()#same as above but for manga
    EmbedDict = Val.to_dict()
    if EmbedDict["title"] != "Error!": 
      Cval = C.GetMangaChapterNumber(EmbedDict["description"])
      if Cval > MVal:
          MVal = Cval
          channel = bot.get_channel(Manga_Channel)
          await channel.send(embed=Val)
    
    await asyncio.sleep(3600)
    #Sleep for 1 hr

async def schedule_daily_message():
  AVal = C.LatestAnimeEpisode()
  MVal = C.LatestMangaChapter()
  await AutoUpdates(AVal,MVal)


@bot.event
async def on_ready():
    print('We can begin the Crafting as {0.user}'.format(bot))
    #this is what is shows when the bot is online

    bot.DelMsg = True
    #For the Auto Delete messages
    await schedule_daily_message()
    #PS- Only 1 such function can work here at a time, as this function was never complete anything below it wouldn't work
    #to trigger the schedule above

    #await tester()

@bot.command()
async def test(ctx): #this is just to see if the IF CONDITION is working
  channel = bot.get_channel(test_channel)
  if bot.DelMsg == True:
    await ctx.message.delete()
  await channel.send("This command is here.")
  AVal = C.LatestAnimeEpisode()
  MVal = C.LatestMangaChapter()
  await AutoUpdates(AVal,MVal,flag=False)
  await channel.send("This command is not here.") 

@bot.command()
async def prefix(ctx):
  if bot.DelMsg == True:
    await ctx.message.delete()
  await ctx.send('$')

@bot.command()
async def hello(ctx):
    if bot.DelMsg == True:
      await ctx.message.delete()
    await ctx.send(f'Hello!  {ctx.author.mention}')
    #reply to the {Prefix}Hello
  
@bot.command()
async def echo(ctx, *, arg):
    if bot.DelMsg == True:
      await ctx.message.delete()
    await ctx.send(arg)
    #Reply to {Prefix}echo arguments, returns the arguments

@bot.command()
async def anime(ctx):
    if bot.DelMsg == True:
      await ctx.message.delete()
    await ctx.send(embed = C.EpisodeUpdate())
    #Reply to {Prefix}anime

@bot.command()
async def manga(ctx):
    if bot.DelMsg == True:
      await ctx.message.delete()
    await ctx.send(embed = C.MangaUpdate())
    #Replt to {Prefix}manga

@bot.command()
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
