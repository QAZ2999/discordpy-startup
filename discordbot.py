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
    await ctx.send('あなたと私の遅延はレベル×１０秒です。')
    
@bot.command()
async def hi(ctx):
    await ctx.send('こんにちは！私は、たなぼっと２４です。よろしくね～(before:Fuck!!)')

@bot.command()
async def hey(ctx):
    await ctx.send('ねぇねぇ、スーパーボールちょうだい！🐱')
 
@bot.command()
async def ha(ctx):
    await ctx.send('は？hahaha')
    
@bot.command()
async def music(ctx):
    await ctx.send('Lets enter command "!p example"')
    
@bot.command()
async def Mee6(ctx):
    await ctx.send('ふはははは。MEE6よ、お前の仕事は私が争奪した（？）"')
    


bot.run(token)
