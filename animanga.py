from bs4 import BeautifulSoup as BS
import requests as r
#Be sure to Install BeautifulSoup and lxml lib
def Get_Soup(link):
  return BS( r.get(link).text, features="lxml")

def Anime():
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

  return EpisodeNumber , EpisodeName , AniMix_Link
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

  soup = Get_Soup(Link)

  #ImageLink = soup.find('img', alt="Read Detective Conan Chapter 1086 - Page 1 For Free In The Highest Quality")["data-lazy-src"]

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

  