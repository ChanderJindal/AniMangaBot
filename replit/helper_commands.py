import discord
from deep_translator import GoogleTranslator

def GetColour(argument):
    switcher = {
    "blue" : discord.colour.Colour.blue(),
    "blurple" : discord.colour.Colour.blurple(),
    "dark_blue" : discord.colour.Colour.dark_blue(),
    "dark_gold" : discord.colour.Colour.dark_gold(),
    "dark_gray" : discord.colour.Colour.dark_gray(),
    "dark_green" : discord.colour.Colour.dark_green(),
    "dark_grey" : discord.colour.Colour.dark_grey(),
    "dark_magenta" : discord.colour.Colour.dark_magenta(),
    "dark_orange" : discord.colour.Colour.dark_orange(),
    "dark_purple" : discord.colour.Colour.dark_purple(),
    "dark_red" : discord.colour.Colour.dark_red(),
    "dark_teal" : discord.colour.Colour.dark_teal(),
    "dark_theme" : discord.colour.Colour.dark_theme(),
    "darker_gray" : discord.colour.Colour.darker_gray(),
    "darker_grey" : discord.colour.Colour.darker_grey(),
    "gold" : discord.colour.Colour.gold(),
    "green" : discord.colour.Colour.green(),
    "greyple" : discord.colour.Colour.greyple(),
    "light_gray" : discord.colour.Colour.light_gray(),
    "light_grey" : discord.colour.Colour.light_grey(),
    "lighter_gray" : discord.colour.Colour.lighter_gray(),
    "lighter_grey" : discord.colour.Colour.lighter_grey(),
    "magenta" : discord.colour.Colour.magenta(),
    "orange" : discord.colour.Colour.orange(),
    "purple" : discord.colour.Colour.purple(),
    "red" : discord.colour.Colour.red(),
    "teal" : discord.colour.Colour.teal(),
    }
    val = switcher.get(argument)
    #print(type(val))
    #print(val)
    ##if val.startswith("0x")
    #return int(switcher.get(argument),base=16)
    string = str(val)[1:]
    return int(string,16)
    #print(string)
    #print( int(string,16))
    #print( int(string,0))
def testing():
    return int(discord.colour.Colour.random(),base=16)

def Translate(msg,to_lang = 'en'):
  return GoogleTranslator(source='auto', target=to_lang).translate(msg)


if __name__ == "__main__":
    print(GetColour("teal"))
    print(discord.Colour.teal())
    #print(int(discord.Colour.teal(),base=10))