from time import sleep
import discord
import commands as C
from discord.ext import commands
import asyncio
import helper_commands as hp
import datetime

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
  if message.author.bot == False and bot.user.mentioned_in(message) and len(message.content) == len(bot.user.mention)+1:
    #make sure the the message is not by any bot, bot is mentioned in message, and the length of message is same as ping length of message + '\n' the Enter/new line character
    #PS:- message.author can give you a ton of info about the message and author
    await message.channel.send(f'Hello! I am the {bot.user.mention}!\nMy Prefix is $')
  else:
    await bot.process_commands(message)

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
##Extra here
@bot.command()
async def getmsg(ctx, channel: discord.TextChannel, msgID: int):
    msg = await channel.fetch_message(msgID)
    '''
    await ctx.send(msg.embeds[0].description)
    await ctx.send(msg.embeds)
    '''

#############################################################
    title_ = None
    author_ = None
    colour_ = None
    description_ = None
    fields_ = None
    footer_ = None
    image_ = None
    provider_ = None
    thumbnail_ = None
    timestamp_ = None
    type_ = None
    url_ = None
    video_ = None
    import goslate
    try:
        title_ = goslate.Goslate().translate(msg.title, 'en')
    except:
        pass
    try:
        author_ = goslate.Goslate().translate(msg.author, 'en')
    except:
        pass
    try:
        colour_ = int(msg.colour)
    except:
        colour_ = 12345678
    try:
        description_ = goslate.Goslate().translate(msg.description, 'en')
    except:
        pass
    try:
        fields_ = goslate.Goslate().translate(msg.fields, 'en')
    except:
        pass
    try:
        footer_ = goslate.Goslate().translate(msg.footer, 'en')
    except:
        pass
    try:
        image_ = msg.image
    except:
        pass
    try:
        provider_ = goslate.Goslate().translate(msg.provider, 'en')
    except:
        pass
    try:
        thumbnail_ = msg.thumbnail
    except:
        pass
    try:
        timestamp_ = msg.timestamp
    except:
        timestamp_ = datetime.datetime.now()
    try:
        type_ = msg.type
    except:
        pass
    try:
        url_ = msg.url
    except:
        pass
    try:
        video_ = msg.video
    except:
        pass

    EmbedVar = discord.Embed(title = title_, 
    author = author_,
    colour = colour_,
    description = description_,
    fields = fields_,
    footer = footer_,
    image = image_,
    provider = provider_,
    thumbnail = thumbnail_,
    timestamp = timestamp_,
    type = type_,
    url = url_,
    video = video_)

    await ctx.send(embed=EmbedVar)

#############################################################
'''
    EmbedVar = hp.TranslateEmbed(msg)
    for i in range(len(EmbedVar)):
      await ctx.send(embed=EmbedVar[i])
'''

import os

tk = os.environ['TOKEN']

bot.run(tk)
