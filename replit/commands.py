import animanga as AM
import discord
import asyncio
from replit import db

##################################### Anime & Manga Updates #####################################

async def EpisodeUpdate():
  try:
      EpNumber , AniMixLink , GogoLink = await AM.Anime()
      embedVar = discord.Embed(title="gogoanime.film's Anime Update", description=f'**Episode#{EpNumber} is available!**', color=5763719)#Green
      embedVar.add_field(name="gogoanime.film 's Link", value=f'{GogoLink}', inline=False)
      embedVar.add_field(name="animixplay.to 's Link", value=f'{AniMixLink}', inline=False)
      #await message.channel.send(embed=embedVar)
      print("HereEP1")
      return embedVar
      #return  f'''ww1.gogoanime2.org says, that Episode#{EpNumber} is available at {GogoLink} You can also find it at {AniMixLink} '''
  except:
      try:
          EpisodeNumber, EpisodeName, AniMixLink, GogoLink =  await AM.AnimeBackup()
          embedVar = discord.Embed(title="myanimelist.net's Anime Update", description=f'**Episode#{EpisodeNumber} - {EpisodeName} is available!**', color=16705372)#Yellow
          embedVar.add_field(name="gogoanime.film 's Link", value=f'{GogoLink}', inline=False)
          embedVar.add_field(name="animixplay.to 's Link", value=f'{AniMixLink}', inline=False)
          print("HereEP2")
          return embedVar
          #return f'''myanimelist.net Says Episode#**{EpisodeNumber}** - ***{EpisodeName}*** is available! You can find them at {GogoLink} {AniMixLink} '''
      except:
          embedVar = discord.Embed(title="Error!", description=f'**Bot is Unable to Detect any Detective Conan Episodes!\nLook at the back-end.**', color=15548997)#Red
          print("HereEP3")
          return embedVar
          #return f'The bot is unable to search any Links for Detecctive Conan Episodes, pls have a look at back end.'

async def MangaUpdate(flag = False):

  try:
      Chapter , MangaDexLink ,GroupName , UploaderName, FrontPage,Name =  await AM.Manga()
      embedVar = discord.Embed(title="MangaDex.org's Manga Update", description=f'**Chapter#{Chapter} - {Name} is available!**', color=5763719)#Green
      embedVar.add_field(name="Group Name", value=f'{GroupName}', inline=True) #Group  & Uploader name are as per API Regulation
      embedVar.add_field(name="Uploader Name", value=f'{UploaderName}', inline=True)
      embedVar.add_field(name="MangaDex.org's Link", value=f'{MangaDexLink}', inline=False)
      try:embedVar.set_image(url=FrontPage)
      except:
          AnimeID = db["MangaDexAnimeID"]
          try:
              AnimeID = await AM.MangaDex_Anime_ID_update()
          except:
              AnimeID = db["MangaDexAnimeID"]
              embedVar.set_image( url = AM.GetCover( AnimeID = AnimeID ) )
      print("HereM1")
      return embedVar
      #return f'''MangaDex has got Chapter#{Chapter}. Read it at {MangaDexLink} '''
  except:
      try:
          Chapter , Link =  await AM.Manga_Backup()
          embedVar = discord.Embed(title="readdetectiveconanarc.com's Manga Update", description=f'**Chapter#{Chapter} is available!**', color=16705372)#Yellow
          embedVar.add_field(name="readdetectiveconanarc.com 's Link", value=f'{Link}', inline=False)
          print("HereM2")
          return embedVar
          #return f'''**readdetectiveconanarc.com** has got Chapter#{Chapter}. Read it at {Link} '''
      except:
          if (flag == False):
              await AM.MangaDex_Anime_ID_update()
              await AM.Last_Chapter_Update()
              return MangaUpdate(True)
          embedVar = discord.Embed(title="Error!", description=f'**Bot is Unable to Detect any Detective Conan Manga!\nLook at the back-end.**', color=15548997)#Red
          print("HereM3")
          return embedVar
      #return f'The bot is unable to search any Links for Detecctive Conan Mangas, pls have a look at back end.'


##################################################### Helper Functions #####################################################

def GetAnimeEpisodeNumber(MyStr):
    lst = MyStr.split(" ")
    MyStr = lst[0][len("**Episode#"):]
    return int(MyStr)

def GetMangaChapterNumber(MyStr):
    lst = MyStr.split(" ")
    MyStr = lst[0][len("**Chapter#"):]
    return int(MyStr)


    
if __name__ == "__main__":
    print(asyncio.run(EpisodeUpdate()))
    print(asyncio.run(MangaUpdate()))
    print(asyncio.run(AM.Anime()))
    print(asyncio.run(AM.AnimeBackup()))
    print(asyncio.run(AM.Manga()))
    print(asyncio.run(AM.Manga_Backup()))