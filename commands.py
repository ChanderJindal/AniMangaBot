import animanga as AM

def EpisodeUpdate():
    try:
        EpNumber , AniMixLink , GogoLink = AM.Anime()
        return f'''ww1.gogoanime2.org says, that
        Episode#{EpNumber} is available at {GogoLink}
        You can also find it at 
        {AniMixLink}
        '''
    except:
        try:
            EpisodeName , EpisodeNumber, AniMixLink, GogoLink = AM.AnimeBackup()
            return f'''myanimelist.net Says
            Episode#**{EpisodeNumber}** - ***{EpisodeName}*** is available!
            You can find them at
            {GogoLink}
            {AniMixLink}
            '''
        except:
            return f'The bot is unable to search any Links for Detecctive Conan Episodes, pls have a look at back end.'

def MangaUpdate():

    try:
        Chapter , MangaDexLink = AM.Manga()
        return f'''MangaDex has got Chapter#{Chapter}. Read it at 
        {MangaDexLink}
        '''
    except:
        try:
            Chapter , Link = AM.Manga_Backup()
            return f'''**readdetectiveconanarc.com** has got Chapter#{Chapter}. Read it at
            {Link}
            '''
        except:
            return f'The bot is unable to search any Links for Detecctive Conan Mangas, pls have a look at back end.'

    
if __name__ == "__main__":
    print(EpisodeUpdate())
    print(MangaUpdate())