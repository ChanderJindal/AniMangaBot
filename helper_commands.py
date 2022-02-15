import discord
def GetColour(argument):
    switcher = {
    "blue" : discord.Colour.blue,
    "blurple" : discord.Colour.blurple,
    "dark_blue" : discord.Colour.dark_blue,
    "dark_gold" : discord.Colour.dark_gold,
    "dark_gray" : discord.Colour.dark_gray,
    "dark_green" : discord.Colour.dark_green,
    "dark_grey" : discord.Colour.dark_grey,
    "dark_magenta" : discord.Colour.dark_magenta,
    "dark_orange" : discord.Colour.dark_orange,
    "dark_purple" : discord.Colour.dark_purple,
    "dark_red" : discord.Colour.dark_red,
    "dark_teal" : discord.Colour.dark_teal,
    "dark_theme" : discord.Colour.dark_theme,
    "darker_gray" : discord.Colour.darker_gray,
    "darker_grey" : discord.Colour.darker_grey,
    "gold" : discord.Colour.gold,
    "green" : discord.Colour.green,
    "greyple" : discord.Colour.greyple,
    "light_gray" : discord.Colour.light_gray,
    "light_grey" : discord.Colour.light_grey,
    "lighter_gray" : discord.Colour.lighter_gray,
    "lighter_grey" : discord.Colour.lighter_grey,
    "magenta" : discord.Colour.magenta,
    "orange" : discord.Colour.orange,
    "purple" : discord.Colour.purple,
    "red" : discord.Colour.red,
    "teal" : discord.Colour.teal
    }
    return switcher.get(argument)