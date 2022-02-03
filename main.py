import discord
import animanga as AM

client = discord.Client()

@client.event
async def on_ready():
    print('We can begin the Crafting as {0.user}'.format(client))

@client.event
async def on_message(message):

  #commnad from bot it self no reply
  if message.author == client.user:
      return

  prefix = "$"

  #await message.channel.send(prefix)
  # check message , removing case-sensitivity , checking prefix
  msg = message.content.lower()

  if msg == "prefix":
    await message.channel.send(prefix)
    return

  if msg.startswith(prefix):
      #message name update
      msg = msg[len(prefix):]
      #await message.channel.send(msg)

      #basic starting test
      if msg.startswith('hello'):
        await message.channel.send('Hello!')
        return
    
      if msg.startswith("echo"):
        await message.channel.send(message.content[len(prefix) + len("echo"):])
        return
    
      if "anime" in msg:
        await message.channel.send(AM.Anime())
        return
      
      if "manga" in msg:
        await message.channel.send(AM.Manga())
        return

from boto.s3.connection import S3Connection
s3 = S3Connection(os.environ['TOKEN'])

client.run(s3)
