#
# Name : Dawid Nalepa
# ID : 2209302
#
import random
import sys
from config import config

# Define the random number generator
def generate_random_numbers(minNumber, maxNumber, howMany):
  return [random.randint(minNumber, maxNumber) for _ in range(howMany)]

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

# Initiating dictionaries outside the event
# Term & Definition dictionry
termDict = {}
# Todo dictionary
todoDict = {}
key = 1


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
    # The * operator in a destructuring assignment to unpack the list and assign the first word 
    # to the unwantedString variable and the rest of the words to userCommandList.
    unwantedString, *userCommandList = msg.split()
    todoMsg = " ".join(userCommandList)
    # Seperating todoMsg to work for term defention
    term, *defenitionList = todoMsg.split()
    defenition = " ".join(defenitionList)
    print(todoMsg)
    print(term)
    print(defenition)

    #
    # IF MESSAGE STARTS WITH : HELLO
    #
    if message.content.startswith(f'{name} hello'):
      await message.channel.send('Hello! I am ALIVE?')

    #
    # IF MESSAGE STARTS WITH : RANDOM 
    #
    elif message.content.startswith(f'{name} random'):
      # If list contains more than 3 parameters
      if len(userCommandList) > 3:
        await message.channel.send('**Exterminate!** Too many parameters!')
      # If list contains less than 3 parameters
      elif len(userCommandList) < 3:
        await message.channel.send('**Exterminate!** Too few parameters!')
      # Otherwise print the numbers
      else:
        if not userCommandList[0].isdigit() or not userCommandList[1].isdigit() or not userCommandList[2].isdigit():
          await message.channel.send('**Exterminate!** Only digits are allowed!')
        # Convert Strings to Integers
        else:
          min : int = int(userCommandList[0])
          max : int = int(userCommandList[1])
          quantity : int = int(userCommandList[2])
          random_numbers = generate_random_numbers(min,max,quantity)
          random_numbers = [str(num) for num in random_numbers]
          # Seperate each number with '&' in the output
          await message.channel.send(f'Random numbers: {" **&** ".join(random_numbers)}')

    #
    # IF MESSAGE STARTS WITH : SUM
    #
    elif message.content.startswith(f'{name} sum'):
      # If list contains more than 2 parameters
      if len(userCommandList) > 2:
        await message.channel.send('**Exterminate!** Too many parameters!')
      # If list contains less than 2 parameters
      elif len(userCommandList) < 2:
        await message.channel.send('**Exterminate!** Too few parameters!')
      # Otherwise print the sum
      else:
        # Checks if the list contains numbers or strings
        if not userCommandList[0].isdigit() or not userCommandList[1].isdigit():
          await message.channel.send('**Exterminate!** Only digits are allowed!')
        # Convert Strings to Integers
        else:
          sum : int = int(userCommandList[0]) + int(userCommandList[1])
          await message.channel.send(f'Sum of numbers is: {sum}')

    #
    # IF MESSAGE STARTS WITH : SET
    #
    elif message.content.startswith(f'{name} set'):
      
      # If term exists Update the definition in dictionary
      if term in termDict:
        termDict[term] = defenition
        await message.channel.send(f'The **definition** has been **updated**')
      # Add term and definition to dictionary
      elif term not in termDict:
        termDict[term] = defenition
        await message.channel.send(f'The **term** and **definition** have been **added**')

        
        
      elif len(userCommandList) == 1: # List only contains the term
        # Delete the term and definition from dictionary
        if userCommandList[0] not in termDict: # Term is not in the dictionary
          await message.channel.send(f'Cannot delete the term: **{term}** as it does **not** exist')
        else: # Term is in the dictionary
          await message.channel.send(f'Successfully **deleted** the term: **{term}**')
          del termDict[term]
        print()

    #
    # IF MESSAGE STARTS WITH : GET
    #
    elif message.content.startswith(f'{name} get'):
      # Checks if the term exists
      if userCommandList[0] not in termDict: # Term does not exist
        await message.channel.send(f'I do **not** know this')
      else: # If term exists, send the message
        await message.channel.send(f'''
**{term}**
**====================**
{termDict[term]}
        ''')

    #
    # IF MESSAGE STARTS WITH : TODO
    #
    elif message.content.startswith(f'{name} todo'):
      if len(todoDict) >= 5:
        await message.channel.send(f'Too **many** items!')
      else:
        # Checks the length of the list to determine whether to add a new item or not
        if len(userCommandList) > 0:
          todoDict[key] = todoMsg
          key += 1
          await message.channel.send(f"The **TODO item** has been **added**")
        elif len(userCommandList) == 0:
          if todoDict:
            todoItems = [f"**{num}:** {todo}" for num, todo in todoDict.items()]
            todoItems = "\n".join(todoItems)
            await message.channel.send(f"**TODO items**\n**================**\n{todoItems}")
          else:
            await message.channel.send("**No TODO items**")

    #
    # IF MESSAGE STARTS WITH : TODOREMOVE
    #
    elif message.content.startswith(f'{name} todoremove'):   
      todoNum = int(userCommandList[0])
      if not userCommandList[0].isdigit():
        await message.channel.send('**Exterminate!** Only digits are allowed!')
      elif todoNum < 1 or todoNum > 5:
        await message.channel.send('**Exterminate!** Please select a number betwenn 1-5')
      elif todoNum in todoDict:
        todoItem = todoDict.pop(todoNum)
        await message.channel.send(f"**TODO item **{todoItem}** has been removed**")
      else:
        await message.channel.send("**No item** with this number**")

    #
    # IF MESSAGE STARTS WITH : HELP
    #
    elif message.content.startswith(f'{name} help'):
      await message.channel.send('''
**Here are some of the commands you can use** 
**=========================================** 
**-> hello**
    **->** Be nice to the bot, say hello :grin:\n
**-> random**
    **->** When asking the chatbot random <minNumber> <maxNumber> <howMany>, 
     it should give a random number between the two numbers and how many random 
     numbers it generates.
    **->** So, for example, random 0 20 2 gives back 2 random numbers. The output should 
     be something like this: Random numbers 13 & 4.\n
**-> sum**
    **->** When asking the chatbot sum <number1> <number2> it should sum up the numbers.
    **->** So, for example, sum 160 20  should return back 180.\n

          ''')

client.run(discordToken)