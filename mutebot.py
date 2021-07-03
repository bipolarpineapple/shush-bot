import discord #for discord bot
import random #for random function

client = discord.Client() #lauch discord client


nsfwWords = ['porn','sex','faggot','nigga','fuck','shit','simp','furry','sit on me', 'sohai',''] #banned word compilation
warningWords = ['"Mine" your word','Mind your tongue','FBI warning','Mind your language','"Mine" your language','Oopsie Woopsie, a banned word had occured '] #warning word compilation

@client.event 
async def on_ready():
    print('{0.user} has initiated'.format(client)) #print on the terminal when the code is running

@client.event
async def on_message(message): 
    nsfw = message.content.lower() #capitalized word will also be recognized

    if message.author == client.user: #bot will not respond to it's own message
        return

    if any(line in nsfw for line in nsfwWords): #for any word in user message that have said the nsfwWords
        warning = random.choice(warningWords) #the bot will random pick a warningWords
        await message.channel.send(warning) #send the warning
    

TOKEN = ' ' #replace if the TOKEN is regenerated
client.run(TOKEN)