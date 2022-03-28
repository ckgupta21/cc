import discord
import os
import requests
import json
import http.client 
import urllib.parse
import random


client=discord.Client()

def get_news():
  response=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=e6c16f9b0fbd4ba69a7b3bccdfdaaa10')
  print(response.content)
  json_data=json.loads(response.content)
  news=json_data['articles'][random.randint(0,10)]['title'] 
  return news

def get_advice():
  response=requests.get('https://api.adviceslip.com/advice')
  print(response.content)
  json_data=json.loads(response.content)
  advice=json_data['slip']['advice']
  return advice
# Registering events on which our bot will respond

# Event when our bot is ready....
@client.event
async def on_ready():
  print('Logged In As {0.user}'.format(client))

# Event when our bot recieves message
  @client.event
  async def on_message(message):
    if message.author==client.user:
      return # Bots will not respond to its own messages
    elif message.content.startswith('hello'):
      await message.channel.send('Hello There!')
    elif message.content.startswith('how are you'):
      await message.channel.send('Iam Fine!! Hope You Are Fine Too')
    elif message.content.startswith('who are the people that made you'):
      await message.channel.send('Ritusman Bhuyan\nChandan Kumar Gupta')
    elif message.content.startswith('who are you'):
      await message.channel.send("Hi! Iam Noobex, Iam a bot made to serve you....")
    elif message.content.startswith('what is your role'):
      await message.channel.send('I show the latest news updates and give some advice to you guys!!')
    elif message.content.startswith('show me some latest news updates'):  
      news=get_news()
      await message.channel.send(news)
    elif message.content.startswith('give me some advice'):
      advice=get_advice()
      await message.channel.send(advice)
    else:
      await message.channel.send("Sorry!! Iam not able to grab it\nIam here to here to help you with showing latest news updates and give some advice....")
      

  
client.run(os.environ['secret_code'])