import discord
import random

def run_program(code):
    globalsParamiter = {'__builtins__': None}
    localsparamiter = {
        '__import__' : __import__,
        'abs': abs, 
        'all': all, 
        'any': any, 
        'ascii': ascii, 
        'bin': bin, 
        'breakpoint': breakpoint, 
        'callable': callable, 
        'chr': chr, 
        'compile': compile, 
        'delattr': delattr, 
        'dir': dir, 
        'divmod': divmod,
        'format': format, 
        'getattr': getattr, 
        'hasattr': hasattr, 
        'hash': hash, 
        'hex': hex, 
        'id': id, 
        'isinstance': isinstance, 
        'issubclass': issubclass, 
        'iter': iter, 
        'len': len, 
        'locals': locals, 
        'max': max, 
        'min': min, 
        'next': next, 
        'oct': oct, 
        'ord': ord, 
        'pow': pow, 
        'print': print, 
        'repr': repr, 
        'round': round, 
        'setattr': setattr, 
        'sorted': sorted, 
        'sum': sum, 
        'vars': vars
        }
    exec(code, globalsParamiter, localsparamiter)
    return f"{code} \n >>> {localsparamiter['final']}"

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
    
@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")
    
    if message.author == client.user:
        return
    
    if message.channel.name == "kremepy": #text channel name

        if user_message == ";help":
            await message.channel.send("Bot description")
            return
        elif user_message[0] == ">":
            await message.channel.send(run_program(user_message[1:]))
            return
        elif user_message == ";list":
            await message.channel.send("Avaliable method")
            return
        else:
            await message.channel.send("Get the help by type ';help")
            return

client.run("MY_TOKEN")
