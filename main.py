import discord
from discord.ext import commands

token = open("token.txt").read()

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("bot online!")

@client.command(pass_context=True)
async def classlist(ctx):
    classes = ""
    member = ctx.message.author
    for i in member.guild.roles:
        classes += (i + "\n")
    await ctx.send("COURSE CATALOG:\n```"+classes+"```")

@client.command(pass_context=True)
async def role(ctx, theRole):
    member = ctx.message.author

    if theRole is None:
        await ctx.send("You have not specified a role")
    else:
        if theRole.isdigit():
            test = discord.utils.get(member.guild.roles, name=theRole)
            if test is None:
                await ctx.send("class " + theRole + " not found!")
            else:
                if test in member.roles:
                    await member.remove_roles(test)
                    await ctx.send("dropped CSE" + theRole)
                else:
                    await member.add_roles(test)
                    await ctx.send("enrolled in CSE" + theRole + "!")
        else:
            await ctx.send("'" + theRole + "' is not a class!")

client.run(token)
