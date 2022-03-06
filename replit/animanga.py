from bs4 import BeautifulSoup as BS
import json
import aiohttp
import asyncio
from replit import db

db["Ep"] = 1037
db["MangaDexAnimeID"] = "7f30dfc3-0b80-4dcc-a3b9-0cd746fac005"
db["Chapter"] = 1088

async def Get_Soup( URL : str , format = "html" ):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
          if format == "json":
            return json.loads(BS( await response.text(), features="lxml").text)
          return BS( await response.text(), features="lxml")

async def Anime():
  Site_Link = "https://gogoanime.film/category/detective-conan"
  Base_Soup = await Get_Soup(Site_Link)

  Main_div = Base_Soup.find('div',class_ = "anime_video_body")

  Sub_div = Main_div.find_all('li')[-1]

  EpNumber = Sub_div.a['ep_end']

  Link_base = "https://gogoanime.film/detective-conan-episode-"

  GogoLink = Link_base + EpNumber.replace(".","-")

  AniMixPlay_Link = f'https://animixplay.to/v1/detective-conan/ep{EpNumber}'

  db["Ep"] = EpNumber

  return EpNumber , AniMixPlay_Link , GogoLink


async def AnimeBackup():
  Site_Link = "https://myanimelist.net/anime/235/Detective_Conan/episode"

  Base_Soup = await Get_Soup(Site_Link)

  EpRange = Base_Soup.find('div', class_ = "pagination ac")

  LatestOne = EpRange.find_all('a',class_ = "link")[-1]

  Correct_Page_Link = LatestOne["href"]

  Correct_Soup = await Get_Soup(Correct_Page_Link)

  LatestEp = Correct_Soup.find_all('a', class_="fl-l fw-b")[-1]

  EpisodeName = LatestEp.text
  EpisodeNumber = LatestEp["href"].split('/')[-1]

  AniMix_Link = f'https://animixplay.to/v1/detective-conan/ep{EpisodeNumber}'
  Gogo_Link = f'https://gogoanime.film/detective-conan-episode-{EpisodeNumber}'

  db["Ep"] = EpisodeNumber

  return EpisodeNumber, EpisodeName ,AniMix_Link, Gogo_Link

###########################################

async def MangaDex_Anime_ID_update():
  name = "detective-conan"
  Api_link = f'https://api.mangadex.org/manga?title={name}'
  json_data = await Get_Soup(Api_link,"json")
  if len(json_data['data']) == 0:
    return "Not Found!"
  Anime_ID = ""
  for i in range(0,10):
    if json_data['data'][i]['attributes']['title']['en'] == "Detective Conan":
      print(str(json_data['data'][i]['attributes']['title']['en']))
      Anime_ID = json_data['data'][i]['id']
      break

  db["MangaDexAnimeID"] = Anime_ID
  return Anime_ID

async def Last_Chapter_Update():
  Site_Link = "https://www.readdetectiveconanarc.com/"

  soup = await Get_Soup(Site_Link)

  Link = soup.find('a', class_ = "column has-text-centered button-last-chapter")
  Link = str(Link["href"])
  #I know it was initially a string, but it was in form of a slice, thus immutable
  Link = Link[0:len(Link)-1]
  Chapter = Link.split('-')[-1]
  db["Chapter"] = Chapter
  return Chapter

async def GroupUploader(json_data):
  if len(json_data['data'][0]["relationships"]) == 3:
    Group_ID = json_data['data'][0]["relationships"][0]["id"]
    Group_link = f'https://api.mangadex.org/group/{Group_ID}'
    Group_data = await Get_Soup(Group_link,"json")
    GroupName = "Not Found"
    if Group_data["result"] == "ok":
      GroupName = Group_data["data"]["attributes"]["name"]
    Uploader_Id = json_data['data'][0]['relationships'][2]['id']
    Uploader_Link = f'https://api.mangadex.org/user/{Uploader_Id}'
    Uploader_data = await Get_Soup(Uploader_Link,"json")
    UploaderName = "Not Found"
    if Uploader_data["result"] == "ok":
      UploaderName = Uploader_data["data"]["attributes"]["username"]

    return GroupName , UploaderName

async def Manga():# For MangaDex 
  Chapter = db["Chapter"]

  Chapter = int(Chapter) + 1 

  Anime_ID = db["MangaDexAnimeID"]
  
  Manga_ID = ""
  GroupName = ""
  UploaderName = ""
  Name = ""
  try:

    link = f'https://api.mangadex.org/chapter?manga={Anime_ID}&chapter={str(Chapter)}&translatedLanguage[]=en'

    json_data = await Get_Soup(link,"json")
    
    Manga_ID = json_data['data'][0]['id']
    GroupName , UploaderName = await GroupUploader(json_data=json_data)
    Name = json_data['data'][0]['attributes']['title']
    db["Chapter"] = Chapter

  except:
      Chapter = int(Chapter) - 1
      link = f'https://api.mangadex.org/chapter?manga={Anime_ID}&chapter={str(Chapter)}&translatedLanguage[]=en'
      json_data = await Get_Soup(link,"json")

      Manga_ID = json_data['data'][0]['id']
      GroupName , UploaderName = await GroupUploader(json_data=json_data)
      Name = json_data['data'][0]['attributes']['title']
  
  PageNumber = 1 

  Final_Link = f'https://mangadex.org/chapter/{Manga_ID}/{PageNumber}'
  ImageLink = await GetFrontPage(MangaID=Manga_ID)
  
  return str(Chapter) , Final_Link , GroupName , UploaderName,ImageLink,Name

async def GetFrontPage(MangaID):
  BaseLink = f"https://api.mangadex.org/at-home/server/{MangaID}"
  json_data = await Get_Soup(BaseLink,"json")
  if json_data["result"] != "ok":
      return json_data["result"]
  Link = json_data["baseUrl"]+"/data/"+json_data["chapter"]["hash"]+"/"
  ImageLink = Link + json_data["chapter"]["data"][0]
  return ImageLink

async def GetCover(AnimeID):
  BaseLink = f'https://api.mangadex.org/manga/{AnimeID}?includes[]=cover_art'

  json_data = await Get_Soup(BaseLink,"json")
  for i in range(0,len(json_data["data"]["relationships"])):
    if json_data["data"]["relationships"][i]["type"] == "cover_art":
      #print(AnimeID)
      #print(json_data["data"]["relationships"][i]["attributes"]["fileName"])
      CoverFileName = json_data["data"]["relationships"][i]["attributes"]["fileName"]
      return f'https://uploads.mangadex.org/covers/{AnimeID}/{CoverFileName}.512.jpg'
      #PS here ".256.jpg" and ".512.jpg" in end are formats, if not specified then it will give original work


async def AllPages(MangaID):#To be used to Read the Manga Not implemented yet
    BaseLink = f"https://api.mangadex.org/at-home/server/{MangaID}"
    json_data = await Get_Soup(BaseLink,"json")
    if json_data["result"] != "ok":
        return json_data["result"]
    Link = json_data["baseUrl"]+"/data/"+json_data["chapter"]["hash"]+"/"
    ImageLst = json_data["chapter"]["data"]
    for i in ImageLst:
        print(Link,i,sep="")
    return "Done"

async def Manga_Backup():
  Site_Link = "https://www.readdetectiveconanarc.com/"

  soup = await Get_Soup(Site_Link)

  Link = soup.find('a', class_ = "column has-text-centered button-last-chapter")
  Link = str(Link["href"])
  #I know it was initially a string, but it was in form of a slice, thus immutable
  Link = Link[0:len(Link)-1]

  Chapter = Link.split('-')[-1]

  return Chapter , Link 
  #f'''
  #New Manga #{Chapter}
  #Link:- {Link}
  #{ImageLink}
  #'''

if __name__ == "__main__":
    a,b,c=asyncio.run(Anime())
    print(a,b,c,sep='\n',end="\n#####\n")
    a,b,c,d=asyncio.run(AnimeBackup())
    print(a,b,c,d,sep='\n',end="\n#####\n")
    a,b,c,d,e,f = asyncio.run(Manga())
    print(a,b,c,d,e,f,sep='\n',end="\n#####\n")
    a,b=asyncio.run(Manga_Backup())
    print(a,b,sep='\n',end="\n#####\n")

'''
#Director's Commentary

If you see "object is not callable", it means you used some thing like 
You want a String and you used
BS(~~The Usual Stuff~~).text() 
what you need it 
BS(~~The Usual Stuff~~).text
that () ruins it

you might be wondering what is lxml?
In that BS(features="lxml") you must had seen it, and yes you need to pip install lxml to get it
it's a format that happens to be most suited for all this

Yes I have removed the Comments from it, but they will still exist in the Requests lib / serial calls one
#It's currently called RequestsCall.py
'''