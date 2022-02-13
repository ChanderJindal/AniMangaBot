from bs4 import BeautifulSoup as BS
import requests as r
import json
#Be sure to Install BeautifulSoup and lxml lib
def Get_Soup(link):
  return BS( r.get(link).text, features="lxml")

def Last_Episode_file_Update(Ep):
    f = open("Last_Episode.txt","w+")
    f.write(Ep)
    f.close()
    return

def Anime():#This is main one - 3 outputs
  #Site_Link = "https://myanimelist.net/anime/235/Detective_Conan/episode" #- slow updates 
  Site_Link = "https://ww1.gogoanime2.org/anime/detective-conan"
  Base_Soup = Get_Soup(Site_Link)
  #Initial Page

  Lower_Half = Base_Soup.find('div',class_ = "anime_video_body")
  #Getting the Lower Half

  Grid_Ep = Lower_Half.find('div',id = "load_ep")
  #Picked the Grid

  List_Ep = Grid_Ep.find('ul', id = "episode_related" )
  # got the unordered list of all the ep ASC

  List_Items = List_Ep.find_all('li')
  #Turned the previous list of CSS into my list

  Latest_Ep = List_Items[-1]
  #the most recent one

  partial_link = Latest_Ep.a["href"]
  #it only carries the later half 
  #Format -> '/watch/detective-conan/1037'
  #I saw an issue with it on site, so i am changing it

  Ep_Number = partial_link.split('/')[-1]

  Link_base = "https://ww1.gogoanime2.org/watch/detective-conan/"
  #This is given

  GogoLink = Link_base + str(Ep_Number)

  #  Ep_Number = Latest_Ep.find('div',class_ = "name").text
  #this returns like 'EP 201'

  Last_Episode_file_Update(Ep_Number)

  #  EP_Type = Latest_Ep.find('div',class_="cate").text
  #to see if it's 'DUB' or 'SUB'

  AniMixPlay_Link = f'https://animixplay.to/v1/detective-conan/ep' + str(Ep_Number)

  #statement = f'{Ep_Number}  {EP_Type}\nThis Episode is Available on\n{AniMixPlay_Link}\n{GogoLink}'

  return Ep_Number , AniMixPlay_Link , GogoLink
  #f'''
  #New Episode #{EpisodeNumber} :- {EpisodeName}
  #Link:- {AniMix_Link}
  #'''

def AnimeBackup():
  Site_Link = "https://myanimelist.net/anime/235/Detective_Conan/episode"

  Base_Soup = Get_Soup(Site_Link)
  #Initial Page

  EpRange = Base_Soup.find('div', class_ = "pagination ac")
  #Getting the range

  LatestOne = EpRange.find_all('a',class_ = "link")[-1]
  #Picked the Last Range

  Correct_Page_Link = LatestOne["href"]

  Correct_Soup = Get_Soup(Correct_Page_Link)
  #Onto the page with Latest Ep

  LatestEp = Correct_Soup.find_all('a', class_="fl-l fw-b")[-1]
  #got the tag with correct info

  EpisodeName = LatestEp.text
  EpisodeNumber = LatestEp["href"].split('/')[-1]

  AniMix_Link = "https://animixplay.to/v1/detective-conan/ep" + str(EpisodeNumber)
  Gogo_Link = "https://ww1.gogoanime2.org/watch/detective-conan/" + str(EpisodeNumber)
  #print(f'''
  #New Episode #{EpisodeNumber} :- {EpisodeName}
  #Link:- {AniMix_Link}
  #'''
  #)
  return EpisodeNumber, EpisodeName ,AniMix_Link, Gogo_Link


########################################################## Manga ##########################################################

def MangaDex_Anime_ID_update():#DC ->Detective Conan 
  name = "detective conan"#this is just for the format
  name = name.replace(" ","-")
  Api_link = f'https://api.mangadex.org/manga?title={name}'


  json_data = r.get(Api_link).json()
  if len(json_data['data']) == 0:
    return False
  Anime_ID = ""
  for i in range(0,10):
    if json_data['data'][i]['attributes']['title']['en'] == "Detective Conan":
      print(str(json_data['data'][i]['attributes']['title']['en']))
      #To make sure that it's the same one,
      Anime_ID = json_data['data'][i]['id']
      break
  # Since I know, that Anime_ID is not supposed to Change
  f = open("Anime_ID.txt","w+")
  f.write(str(Anime_ID))
  f.close()
  return Anime_ID

def Last_Chapter_file_Update(Chapter):
    f = open("Last_Chapter.txt","w+")
    f.write(str(Chapter))
    f.close()
    return

def Last_Chapter_Update():
  Site_Link = "https://www.readdetectiveconanarc.com/"

  soup = Get_Soup(Site_Link)

  Link = soup.find('a', class_ = "column has-text-centered button-last-chapter")
  Link = str(Link["href"])
  #I know it was initially a string, but it was in form of a slice, thus immutable
  Link = Link[0:len(Link)-1]
  Chapter = Link.split('-')[-1]
  Last_Chapter_file_Update(Chapter)
  return Chapter

def Manga():# For MangaDex 
  Chapter = 1087
  try:#If we got the Last_Chapter Number good, otherwise call the function above and make API call and get it
    f = open("Last_Chapter.txt","r")
    Chapter = f.read()
    f.close()
  except:
    Chapter = Last_Chapter_Update()

  Chapter = int(Chapter) + 1 #incase an update has been made

  Anime_ID = ""

  try:#If Anime ID is in file cool, otherwise make an API call
    f = open("Anime_ID.txt","r")
    Anime_ID = f.read()
    f.close()
  except:
    Anime_ID = MangaDex_Anime_ID_update()
  
  Manga_ID = ""
  #print(Anime_ID,Chapter)
  try:
  #Got the one for the newest expected Chapter
    link = f'https://api.mangadex.org/chapter?manga={Anime_ID}&chapter={str(Chapter)}&translatedLanguage[]=en'
    #Passing chapter as a string is best
    response = r.get(link)
    json_data = response.json()
    #print(link)
    Manga_ID = json_data['data'][0]['id']

    Last_Chapter_file_Update(Chapter=str(Chapter))
    #Since now it's Chapter + 1

  except:
    #So, chapter +1 is now out yet, so back to previous one
      #print("here1")
      Chapter = int(Chapter) - 1
      link = f'https://api.mangadex.org/chapter?manga={Anime_ID}&chapter={str(Chapter)}&translatedLanguage[]=en'
      response = r.get(link)
      json_data = response.json()
      #print(link)
    #Since last chapter update function sent me this detail, this chapter exists for sure
      Manga_ID = json_data['data'][0]['id']

  
  #^This is the main Thing!

  PageNumber = 1 #This one is for sake of format only

  Final_Link = f'https://mangadex.org/chapter/{Manga_ID}/{PageNumber}'
  
  return str(Chapter) , Final_Link

def Manga_Backup():
  Site_Link = "https://www.readdetectiveconanarc.com/"

  soup = Get_Soup(Site_Link)

  Link = soup.find('a', class_ = "column has-text-centered button-last-chapter")
  Link = str(Link["href"])
  #I know it was initially a string, but it was in form of a slice, thus immutable
  Link = Link[0:len(Link)-1]

  Chapter = Link.split('-')[-1]

  '''
  To get first Page of Manga, but it already comes with the manga link
  soup = Get_Soup(Link)
  ImageLink = soup.find('img', alt="Read Detective Conan Chapter "+str(Chapter)+" - Page 1 For Free In The Highest Quality")["data-lazy-src"]
  '''

  return Chapter , Link 
  #f'''
  #New Manga #{Chapter}
  #Link:- {Link}
  #{ImageLink}
  #'''



if __name__ == "__main__":
  print("Here")
  print(Anime())
  print(MangaDex_Anime_ID_update())
  print("Here")
  print(Manga())
  print("Here")

  