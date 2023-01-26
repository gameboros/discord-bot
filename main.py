import os
import discord
import pafy
import random

my_secret = 'your token'


FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}

search = 'ben saying no'

voice_client = ''

#2733784431680
intents=discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('{0.user} está online'.format(client))

@client.event
async def on_message(message):
  print(message.content)
  if message.content == 'message you wanna match':
    # Get the audio file name from the message
        #audio_file = message.content[5:]

    # Search for the audio file on YouTube
    video = pafy.new(f"video url you wanna play")
    bestaudio = video.getbestaudio()

    voice_client = discord.utils.get(client.voice_clients)
    # Join the user's voice channel
    if voice_client:
      print('Already connected')
    else:
      voice_channel = message.author.voice.channel
      voice_client = await voice_channel.connect()
      
    if voice_client:
      voice_client.play(discord.FFmpegOpusAudio(executable = 'your ffmpeg address' , source=bestaudio.url))

def sendtxt(name: str): #le os caules(txts da pasta)
  file1 = open('txts/'+name+'.txt', 'r')
  Lines = file1.readlines()
  string_return = ""
  for line in Lines: string_return += line
  file1.close()
  return string_return




client.run(my_secret)
