import discord
from discord.ext import commands

# Credentials
TOKEN = 'ODEzOTYxNDQ2MTkwMDg4MjEw.YDW6qw.uLQxjG2z0dKzb3K7qBwOUhpOvY8'

# Creating the Bot
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("Connected to bot: {}".format(client.user.name))
    print("Bot ID: {}".format(client.user.id))


# Command

@client.command()
async def hello_world(ctx):
    await ctx.send("Hello World!")

# Running the bot
client.run(TOKEN)
