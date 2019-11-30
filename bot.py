import discord
import random
import os
from discord.ext import commands
from discord.ext.commands import Bot
#TOKEN = 'NjUwMTE5MTgxMzQ1MzU3ODI0.XeGvuQ._SYEHt5WALfjoSigfTaYT3SrCDM'


Bot = commands.Bot(command_prefix=')')

@Bot.event
async def on_ready():
	print("hello")

@Bot.command(pass_context= True) 
async def дворовые(ctx):
	await ctx.send("рейвы")

@Bot.command(pass_context= True) 
async def Дима(ctx):
	await ctx.send("пидор")

@Bot.command(pass_context=True)
async def test(ctx, arg):
    await ctx.send(arg)

@Bot.command(pass_context= True) 
async def roll(ctx):
	await ctx.send(random.randint(1,100))

@Bot.command(pass_context=True)
async def чел(ctx):
	await ctx.send("Пидор {}".format(ctx.message.author.mention))

@Bot.command(pass_context= True) 
async def inf(ctx, user: discord.User):
	await ctx.send(user.created_at)

@Bot.command(pass_context= True) 
async def inf2(ctx, user: discord.User):
	await ctx.send(user.avatar_url)

token = environ.get('BOT_TOKEN')
