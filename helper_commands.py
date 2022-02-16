import discord
def GetColour(argument):
    switcher = {
    "blue" : discord.colour.Colour.blue()(),
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
    "teal" : discord.colour.Colour.teal()
    }
    return int(switcher.get(argument),base=16)
def testing():
    return discord.colour.Colour.random

if __name__ == "__main__":
    print(discord.Colour.teal())