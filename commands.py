import animanga as AM

def EpisodeUpdate():
    Current_Number , name , link = AM.Anime()
    try:
        f= open("Latest_Ep.txt",mode='r')
        Last_Number = f.read()
        f.close()
        if Last_Number == Current_Number:
            return f'''No Updates Yet. Lastest Episode till now is:-
            Episode Number#{Current_Number} :- {name}
            can be found at {link}
            '''
        else:
            f.open("Latest_Ep.txt",mode = 'w+')
            f.write(Current_Number)
            f.close()
            return f'''The Latest Episode is out!
            Episode Number#{Current_Number} :- {name}
            can be found at {link}
            '''
    except:
        f.open("Latest_Ep.txt",mode = 'w+')
        f.write(Current_Number)
        f.close()
        return f'''The Current Latest Episode is:-
        Episode Number#{Current_Number} :- {name}
        can be found at {link}
        '''

def MangaUpdate():
    Current_Number , link = AM.Manga()
    try:
        f= open("Latest_Manga.txt",mode='r')
        Last_Number = f.read()
        f.close()
        if Last_Number == Current_Number:
            return f'''No Updates Yet. Lastest Manga till now is:-
            Manga Edition#{Current_Number} 
            can be found at {link}
            '''
        else:
            f.open("Latest_Manga.txt",mode = 'w+')
            f.write(Current_Number)
            f.close()
            return f'''The Latest Manga is out!
            Manga Edition#{Current_Number}
            can be found at {link}
            '''
    except:
        f.open("Latest_Manga.txt",mode = 'w+')
        f.write(Current_Number)
        f.close()
        return f'''The Current Latest Manga is:-
        Manga Edition#{Current_Number}
        can be found at {link}
        '''
