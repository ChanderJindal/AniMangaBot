import discord
import goslate

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

def TranslateEmbed(msg):
    if type(msg) == "<class 'discord.embeds.Embed'>":
      title_ = None
      author_ = None
      colour_ = None
      description_ = None
      fields_ = None
      footer_ = None
      image_ = None
      provider_ = None
      thumbnail_ = None
      timestamp_ = None
      type_ = None
      url_ = None
      video_ = None

      MsgDict = msg.to_dict()

      try:
        title_ = goslate.Goslate().translate(MsgDict["title"], 'en')
      except:
        pass
      try:
        author_ = goslate.Goslate().translate(MsgDict["author"], 'en')
      except:
        pass
      try:
        colour_ = MsgDict["colour"]
      except:
        pass
      try:
        description_ = goslate.Goslate().translate(MsgDict["description"], 'en')
      except:
        pass
      try:
        fields_ = goslate.Goslate().translate(MsgDict["fields"], 'en')
      except:
        pass
      try:
        footer_ = goslate.Goslate().translate(MsgDict["footer"], 'en')
      except:
        pass
      try:
        image_ = MsgDict["image"]
      except:
        pass
      try:
        provider_ = goslate.Goslate().translate(MsgDict["provider"], 'en')
      except:
        pass
      try:
        thumbnail_ = MsgDict["thumbnail"]
      except:
        pass
      try:
        timestamp_ = MsgDict["timestamp"]
      except:
        pass
      try:
        type_ = MsgDict["type"]
      except:
        pass
      try:
        url_ = MsgDict["url"]
      except:
        pass
      try:
        video_ = MsgDict["video"]
      except:
        pass

      EmbedVar = discord.Embed(title = title_, 
      author = author_,
      colour = colour_,
      description = description_,
      fields = fields_,
      footer = footer_,
      image = image_,
      provider = provider_,
      thumbnail = thumbnail_,
      timestamp = timestamp_,
      type = type_,
      url = url_,
      video = video_)

      return EmbedVar

def Translate(msg,to_lang = 'en'):
    return goslate.Goslate().translate(msg, to_lang)


if __name__ == "__main__":
    print(GetColour("teal"))
    print(discord.Colour.teal())
    #print(int(discord.Colour.teal(),base=10))