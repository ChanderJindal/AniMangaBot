from time import sleep
import discord
import commands as C
from discord.ext import commands
import asyncio
import helper_commands as hp


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

bot = commands.Bot(command_prefix='$', case_insensitive=True)
#This is to check prefix, yes prefix can be changed using file system

@bot.event
async def on_ready():
    print('We can begin the Crafting as {0.user}'.format(bot))
    #this is what is shows when the bot is online

    bot.DelMsg = True
    #For the Auto Delete messages

    bot.prefix = '$'
    await schedule_daily_message()
    #PS- Only 1 such function can work here at a time, as this function was never complete anything below it wouldn't work
    #to trigger the schedule above

    #await tester()

@bot.event#ping reply
async def on_message(message):
  if bot.user.mentioned_in(message) and len(message.content) == len(bot.user.mention)+1:
    #make sure the the message is not by any bot, bot is mentioned in message, and the length of message is same as ping length of message + '\n' the Enter/new line character
    #PS:- message.author can give you a ton of info about the message and author
    await message.channel.send(f'Hello! I am the {bot.user.mention}!\nMy Prefix is $')
  else:
    await bot.process_commands(message)

@bot.event
async def AutoTranslate(message):
  if message.author.bot == True and message.channel.id == 774934515817644043: #<- this is #twitter channel of server
    embeds = message.embeds #rest is same as {getmsg}
    for e in embeds:
      var = e.to_dict()
      try:
        var["footer"]["text"] = hp.Translate(var["footer"]["text"])
      except:pass
      try:
        var["author"]["name"] = hp.Translate(var["author"]["name"])
      except:pass
      try:
        var["description"] = hp.Translate(var["description"])
      except:pass
      await message.channel.send(embed=discord.Embed.from_dict(var))
  else:
      await bot.process_commands(message)#to process on this command further,
# 829814770453839895
@bot.event
async def AutoTranslateTest(message):
  if message.author.bot == True and message.channel.id == 829814770453839895: #<- this is #general channel of BCT
    embeds = message.embeds #rest is same as {getmsg}
    for e in embeds:
      var = e.to_dict()
      try:
        var["footer"]["text"] = hp.Translate(var["footer"]["text"])
      except:pass
      try:
        var["author"]["name"] = hp.Translate(var["author"]["name"])
      except:pass
      try:
        var["description"] = hp.Translate(var["description"])
      except:pass
      await message.channel.send(embed=discord.Embed.from_dict(var))
  else:
      await bot.process_commands(message)#to process on this command further,

@bot.command(name='SetPrefix',aliases=['changePrefix','NewPrefix'])
async def SetPrefix(ctx,arg):
  temp = bot.DelMsg
  bot = commands.Bot(command_prefix=arg, case_insensitive=True)
  bot.prefix = arg
  bot.DelMsg = temp
  ctx.send(f'The New Prefix is {bot.prefix}')

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

@bot.command(name='hello',aliases=['hey','hola'])
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

@bot.command(name='anime',aliases=['A'])
async def anime(ctx):
    if bot.DelMsg == True:
      await ctx.message.delete()
    await ctx.send(embed = C.EpisodeUpdate())
    #Reply to {Prefix}anime

@bot.command(name='manga',aliases=['M'])
async def manga(ctx):
    if bot.DelMsg == True:
      await ctx.message.delete()
    await ctx.send(embed = C.MangaUpdate())
    #Replt to {Prefix}manga

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

@bot.command()
async def MakeEM(ctx):
  #A try to make an embed message from user input in 3 steps, colour , title and content
  try:
    await ctx.send("Enter Title of the EmbededMessage.")
    title_message = await bot.wait_for('message', timeout=10.0)
  except:
    title_message = f"__{ctx.author}'s Message__"
  sleep(10)
  try:
    await ctx.send("Enter Description of the EmbededMessage.")
    description_message = await bot.wait_for('message', timeout=10.0)
  except:
      description_message = f"*{ctx.author}*'s Description."
  sleep(10)
  try:
    await ctx.send("Pick a colour for the message.\n`blue`, `blurple`, `dark_blue`, `dark_gold`, `dark_gray`, `dark_green`, `dark_grey`, `dark_magenta`, `dark_orange`, `dark_purple`, `dark_red`, `dark_teal`, `dark_theme`, `darker_gray`,  `darker_grey`, `gold`, `green`, `greyple`, `light_gray`, `light_grey`, `lighter_gray`, `lighter_grey`, `magenta`, `orange`, `purple`, `red`, `teal`.\nOr Enter the Int Value Code.")
    #Giving out the choices of color available

    color_message = await bot.wait_for('message', timeout=10.0)
    IntVal = int( str(discord.colour.Colour.random())[1:],base=16)#removing the #
    #'discord.colour.Colour'
    try:
      #in case of int
      IntVal = int(color_message.context)
    except:
      #in case of Hex
      try:
        IntVal = int(str(color_message.context)[1:],base=16)
      except:
        #type a color from list sent
        try: 
          IntVal = hp.GetColour(color_message.context[0])
        except:
          pass
    color_message = IntVal
  except:
    #if no message
    color_message = int( str(discord.colour.Colour.random())[1:],base=16)
  
  EmbedVar = discord.Embed(title=str(title_message),description=str(description_message),colour=int(str(color_message)))

  await ctx.send(embed=EmbedVar)


@bot.command() #It takes in an embed message and translates it into english then returns it
async def getmsg(ctx, channel: discord.TextChannel, msgID: int):
  #you need to specify the channel from where the message is picked <#Channel.id> format then, message ID, 
  #PS:- The channel must be present in server
    msg = await channel.fetch_message(msgID)#got the message
    embeds = msg.embeds #embeded part
    for e in embeds:
      var = e.to_dict()# made it into a dict(), it's easier to process

      #On test case these 3 were in jp / ja converted them to en
      try:#use try block to see if it is present
        var["footer"]["text"] = hp.Translate(var["footer"]["text"])
      except:pass#if it's already in eng no need to change it, or if it can't it's better to give the original part, instead of nothing
      try:
        var["author"]["name"] = hp.Translate(var["author"]["name"])
      except:pass
      try:
        var["description"] = hp.Translate(var["description"])
      except:pass
      await ctx.send(embed=discord.Embed.from_dict(var))

@bot.command()#just for testing
#this is same as {getmsg} but it only gives the dict() to see the stuff in message 
async def getmsgdict(ctx, channel: discord.TextChannel, msgID: int):
  msg = await channel.fetch_message(msgID)
  embeds = msg.embeds 
  for e in embeds:
    await ctx.send(e.to_dict())


import os

tk = os.environ['TOKEN']

bot.run(tk)
