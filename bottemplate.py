import sys
from config import config
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

    # del list[0]
    # sum : int = int(list[0]) + int(list[1])
    # print(sum)

    # IF MESSAGE STARTS WITH : HELLO
    if message.content.startswith(f'{name} hello'):
      await message.channel.send('Hello! I am ALIVE?')

    # IF MESSAGE STARTS WITH : RANDOM 
    elif message.content.startswith(f'{name} random'):
      # if list contains more than 3 parameters
      if len(list) > 3:
        await message.channel.send('Exterminate! Too many parameters!')
      # if list contains less than 3 parameters
      elif len(list) < 3:
        await message.channel.send('Exterminate! Too many parameters!')
      # otherwise print the numbers
      else:
        await message.channel.send('Random numbers _ & _')

    # IF MESSAGE STARTS WITH : SUM
    elif message.content.startswith(f'{name} sum'):
      if len(list) > 3:
        await message.channel.send('Exterminate! Too many parameters!')
      elif len(list) < 2:
        await message.channel.send('Exterminate! Too few parameters!')
      else:
        # sum : int = int(list[0]) + int(list[1])
        await message.channel.send(f'Sum of numbers is: {sum}')

    # IF MESSAGE STARTS WITH : HELP
    elif message.content.startswith(f'{name} help'):
      await message.channel.send('Here are some of the commands you can use\n' +
                                 '=========================================\n' +
                                 '-> Random\n' +
                                 '  ->\n' +
                                 '-> Sum\n' +
                                 '  ->\n' +
                                 '-> ')

client.run(discordToken)