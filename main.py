import discord
import random
import asset

def run_program(code):
    globalsParamiter = {'__builtins__': None}
    localsparamiter = asset.asset['avaliable_method']
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
            await message.channel.send(asset.asset['help_description'])
            return
        elif user_message[0] == ">":
            await message.channel.send(run_program(user_message[1:]))
            return
        elif user_message == ";list":
            string = ""
            for method in asset.asset["avaliable_method"]:
                string += "   -" + str(method) + '\n'
            await message.channel.send(asset.asset['list_description'] + string)
            return
        elif user_message == ";code":
            await message.channel.send(asset.asset['code_github'])
            return
        else:
            await message.channel.send("Get the help by type ';help")
            return

client.run(asset.asset['TOKEN'])
