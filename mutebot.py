import discord #for discord bot
import random #for random function
from discord.ext import commands
import asyncio

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


@client.command() #guide
async def helpmenu(ctx):
    helpmsg = discord.Embed(title=f"Tips for using {client.user}",
                         description="> **'+mute <@member> <reason>'**\n"
                                     "mute member with a reason(reason is optional)\n\n"

                                     "> **'+unmute <@member>'**\n"
                                     "unmute member\n\n"

                                     "> **'+tempmute <@member> <time> <unit(s,m,h,d)> <reason>'**\n"
                                     "time mute member [s=seconds, m=minutes, h=hours, d=days](reason is optional)",
                              colour=discord.Colour.magenta())

    await ctx.send(embed=helpmsg)


@client.command() #manually mute members
@commands.has_permissions(kick_members=True)
async def mute(ctx, member : discord.Member, *,reason=None):
    role = ctx.guild.get_role()
    await ctx.send(f"Muted because of {reason}")
    await member.add_roles(role, reason=reason)
    
    
@client.command() #manually unmute member
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member : discord.Member):
    if not member:
        await ctx.send('Remember to @ the member')
    else:
        role = ctx.guild.get_role()
        await ctx.send("Unmuted")
        await member.remove_roles(role)

@client.command() #timed mute
@commands.has_permissions(kick_members=True)
async def tempmute(ctx, member : discord.Member=None,time=0,unit=None,*,reason=None): #user will need to enter the "$" with member's name and their reason
    if not member:
        await ctx.send("Don't forget to @ the member")
        return
    elif not time:
        await ctx.send("Don't forget about the time")
        return
    elif not unit:
        await ctx.send("Don't forget about the unit")
        return
    else:
        role = ctx.guild.get_role() #remember to change in different server for the role
        await member.add_roles(role, reason=reason) #add the "role" to the user and the reason too
        await ctx.send(f"Muted because of {reason} for {time}{unit}") #message
        if unit == 's':
            duration = 1 * time
            await asyncio.sleep(duration)
        elif unit == 'm':
            duration = 60 * time
            await asyncio.sleep(duration)
        elif unit == 'h':
            duration = 60 * 60 * time
            await asyncio.sleep(duration)
        elif unit == 'd':
            duration = 24 * 60 * 60 * time 
            await asyncio.sleep(duration)
        await member.remove_roles(role)
        await ctx.send("Times up! Unmuted")


TOKEN = ' ' #replace if the TOKEN is regenerated
client.run(TOKEN)
