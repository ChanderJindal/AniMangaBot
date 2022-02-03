import animanga as AM

def MakeEpFile(Num):
    f = open("Latest_Ep.txt",mode = "w")
    f.write(str(Num))
    f.close()

def MakeMangaFile(Num):
    f = open("Latest_Manga.txt",mode = "w")
    f.write(str(Num))
    f.close()

def EpisodeUpdate():
    Current_Number , name , link = AM.Anime()
    try:
        f1= open("Latest_Ep.txt",mode='r')
        Last_Number = f1.read()
        f1.close()
        if Last_Number == Current_Number:
            return f'''No Updates Yet. Lastest Episode till now is:-
            Episode Number#{Current_Number} :- {name}
            can be found at {link}
            '''
        else:
            MakeEpFile(Current_Number)
            return f'''The Latest Episode is out!
            Episode Number#{Current_Number} :- {name}
            can be found at {link}
            '''
    except:
        MakeEpFile(Current_Number)
        return f'''The Current Latest Episode is:-
        Episode Number#{Current_Number} :- {name}
        can be found at {link}
        '''

def MangaUpdate():
    Current_Number , link = AM.Manga()
    try:
        f1= open("Latest_Manga.txt",mode='r')
        Last_Number = f1.read()
        f1.close()
        if Last_Number == Current_Number:
            return f'''No Updates Yet. Lastest Manga till now is:-
            Manga Edition#{Current_Number} 
            can be found at {link}
            '''
        else:
            MakeMangaFile(Current_Number)
            return f'''The Latest Manga is out!
            Manga Edition#{Current_Number}
            can be found at {link}
            '''
    except:
        MakeMangaFile(Current_Number)
        return f'''The Current Latest Manga is:-
        Manga Edition#{Current_Number}
        can be found at {link}
        '''
if __name__ == "__main__":
    print(EpisodeUpdate())
    print(MangaUpdate())