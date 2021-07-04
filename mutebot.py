import discord #for discord bot
import random #for random function
from discord.ext import commands

client = commands.Bot(command_prefix="+") #lauch discord client

nsfwWords = ['porn','sex','faggot','nigga','fuck','shit','simp','furry','sit on me','jav','nigger'] #banned word compilation
warningWords = ['"Mine" your word','Mind your tongue','FBI warning','Mind your language','"Mine" your language'] #warning word compilation

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
        await message.delete()

    await client.process_commands(message)

@client.command() #mute members
@commands.has_permissions(kick_members=True)
async def mute(ctx, member : discord.Member, *,reason=None):
    role = ctx.guild.get_role(860927818149658664)
    await ctx.send(f"Muted because of {reason}")
    await member.add_roles(role, reason=reason)
    
    
@client.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member : discord.Member):
    role = ctx.guild.get_role(860927818149658664)
    await ctx.send("has been unmuted")
    await member.remove_roles(role)
    

TOKEN = 'ODYwODI1NzkxMzg2MzUzNjc1.YOA4fg.9mdIkAD1E21Aw_LtIunYtwAff94' #replace if the TOKEN is regenerated
client.run(TOKEN)