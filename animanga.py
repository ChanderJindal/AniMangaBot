from bs4 import BeautifulSoup as BS
import requests as r
#Be sure to Install BeautifulSoup and lxml lib
def Get_Soup(link):
  return BS( r.get(link).text, features="lxml")

def Anime():
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

  Link_Part_2 = Latest_Ep.a["herf"]
  #it only carries the later half 

  Link_Part_1 = "https://ww1.gogoanime2.org/"
  #This is given

  Link_Full = Link_Part_1 + Link_Part_2

  Ep_Number = Latest_Ep.find('div',class_ = "name").text
  #this returns like 'EP 201'

  EP_Type = Latest_Ep.find('div',class_="cate").text
  #to see if it's 'DUB' or 'SUB'

  AniMixPlay_Link = f'https://animixplay.to/v1/detective-conan/' + str(Ep_Number).lower().replace(" ","")

  #statement = f'{Ep_Number}  {EP_Type}\nThis Episode is Available on\n{AniMixPlay_Link}\n{Link_Full}'

  return Ep_Number , AniMixPlay_Link , Link_Full,EP_Type
  #f'''
  #New Episode #{EpisodeNumber} :- {EpisodeName}
  #Link:- {AniMix_Link}
  #'''
def Manga():
  Site_Link = "https://www.readdetectiveconanarc.com/"

  soup = Get_Soup(Site_Link)

  Link = soup.find('a', class_ = "column has-text-centered button-last-chapter")
  Link = str(Link["href"])
  #I know it was initially a string, but it was in form of a slice, thus immutable
  Link = Link[0:len(Link)-1]

  Edition = Link.split('-')[-1]

  '''
  To get first Page of Manga, but it already comes with the manga link
  soup = Get_Soup(Link)
  ImageLink = soup.find('img', alt="Read Detective Conan Chapter "+str(Edition)+" - Page 1 For Free In The Highest Quality")["data-lazy-src"]
  '''

  return Edition , Link 
  #f'''
  #New Manga #{Edition}
  #Link:- {Link}
  #{ImageLink}
  #'''

if __name__ == "__main__":
  print("Here")
  print(Anime())
  print("Here")
  print(Manga())
  print("Here")

  