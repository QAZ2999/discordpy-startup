from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def hi(ctx):
    await ctx.send('Fuck!!')
    
@bot.command()
async def ？(ctx):
    await ctx.send('単品「？」は嫌いです。セットでお願いします。')
    
@bot.command()
async def ?(ctx):
    await ctx.send('単品「？」は嫌いです。セットでお願いします。?')

bot.run(token)
