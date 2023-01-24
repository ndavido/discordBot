import sys
# Your bot token here
discordToken = "MTA2NTkxNjUzNDE3MTYzOTg3OQ.GL-kbw.Ace6SxxeHRhnnN-qwexqMxd5vg_X_ekNIYxFTY"
# Your bot name here
name = "csm101_dawid_nalepa"

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

    if message.content.startswith(f'{name} hello'):
      await message.channel.send('Hello! I am ALIVE?')

    if message.content.startswith(f'{name} random'):
      await message.channel.send('Random is yet to be implemented!')

    elif message.content.startswith(f'{name} sum'):
      await message.channel.send('Sum is yet to be implemented!')

client.run(discordToken)