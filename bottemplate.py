import sys
from .config import config
# Insert your bot token here
discordToken = config.get("bot_token")
# Insert your bot name here
name = config.get("bot_name")

# Check if Token is empty
if (discordToken == ""): sys.exit("ERROR: Please set the discord token.")
# Check if Name is empty
if (name == ""): sys.exit("ERROR: Please set the name of the bot.")

# Import discord
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user: return # We don't want to reply to ourselves

  # RULE: To not flood the channel with responses from multiple bots,
  # we only respond to messages that start with our name

  if message.content.startswith(name):
    print(f"{message.author} says: {message.content}")

    msg = message.content[len(name):].strip()
    print(f"msg contains: {msg}")
    list = msg.split(" ")
    print(list)
    # if len(msg)

    if message.content.startswith(f'{name} hello'):
      await message.channel.send('Hello! I am ALIVE?')

    elif message.content.startswith(f'{name} random'):
      await message.channel.send('Random numbers _ & _')

    elif message.content.startswith(f'{name} sum'):
      await message.channel.send('Sum of numbers is: _')

    elif message.content.startswith(f'{name} help'):
      await message.channel.send('Here are some of the commands you can use\n' +
                                 '=========================================\n' +
                                 '-> Random\n' +
                                 '-> Sum' +
                                 '-> ')

client.run(discordToken)