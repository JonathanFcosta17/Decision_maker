import discord
import os
from decision_class import DecisionMaker
from dotenv import load_dotenv

# Creating the bot


class MyClient(discord.Client):
    async def on_ready(self):  # When the bot is ready
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):  # When the bot receives a message
        print('Message from {0.author}: {0.content}'.format(message))

        name = message.author.mention  # Get the name of the user that sent the message

# English language
        # Creating !help command
        if message.content.startswith('!hello'):
            await message.channel.send(f"Hello {name}!")

        # Creating !choice command
        if message.content.startswith('!choice'):
            await message.channel.send(f"Welcome to the Decision Maker!{os.linesep}Enter a list of options separated by commas:{os.linesep}Example: 'Option 1, Option 2, Option 3'.")

            # Checking if the user that is using the bot is the same that sent the message
            def check(msg):
                return msg.author == message.author and msg.channel == message.channel

            # Waiting for the user to send the options
            options = await self.wait_for('message', check=check)

            # Creating a decision maker object
            decision = DecisionMaker(options.content)

            # Asking if the user wants to add weights
            await message.channel.send(f"Would you like to add some weight to the options?{os.linesep}Enter 'y' for yes and 'n' for no.")

            # Looping until the user enters a valid answer
            while True:
                # Waiting for the user to send the answer
                answer = await self.wait_for('message', check=check)
                # Getting the first letter of the answer
                answer = answer.content.lower()[0]

                if answer == 'n':
                    # If the user doesn't want to add weights
                    await message.channel.send(f"{name} asked The Great Decision Maker what to do.{os.linesep}The Great Decision Maker says: ***{decision.make_decision_simple()}***")
                    break

                elif answer == 'y':

                    try:
                        # If the user wants to add weights
                        await message.channel.send(f"This is the list of options that you entered: {options.content}")
                        await message.channel.send("Enter the weights separared by commas as well(Example: '1, 2, 3'):")
                        # Waiting for the user to send the weights
                        weights = await self.wait_for('message', check=check)
                        # Sending the decision
                        await message.channel.send(f"{name} asked The Great Decision Maker what to do.{os.linesep}The Great Decision Maker says: ***{decision.make_decision_weighted(weights.content)}***")
                        break

                    except Exception as e:
                        await message.channel.send(f"Invalid input{os.linesep}{e}")
                        await message.channel.send("Enter the weights separared by commas as well(Example: '1, 2, 3'):")
                        # Waiting for the user to send the weights
                        weights = await self.wait_for('message', check=check)
                        # Sending the decision
                        await message.channel.send(f"{name} asked The Great Decision Maker what to do.{os.linesep}The Great Decision Maker says: ***{decision.make_decision_weighted(weights.content)}***")
                        break

                else:
                    await message.channel.send("Invalid input")

        # Creating !help command
        if message.content.startswith('!help'):
            await message.channel.send(f"""Hello!{os.linesep}I'm The Great Decision Maker, I was created by Jonathan Costa to help you make decisions.{os.linesep}{os.linesep}The commands are: {os.linesep}***!hello*** - Says hello to you{os.linesep}***!choice*** - Starts the bot{os.linesep}***!help*** - Shows this message{os.linesep}{os.linesep}The bot is open source and you can find it here:
https://github.com/JonathanFcosta17/Decision_maker""")


# Portuguese language
        # Creating !ola command
        if message.content.startswith('!ola'):
            await message.channel.send(f"Olá {name}!")

        # Creating !escolha command
        if message.content.startswith('!escolha'):
            await message.channel.send(f"Bem-vindo ao Decision Maker!{os.linesep}Digite uma lista de opções separadas por vírgulas:{os.linesep}Exemplo: 'Opção 1, Opção 2, Opção 3'.")

            # Checking if the user that is using the bot is the same that sent the message
            def check(msg):
                return msg.author == message.author and msg.channel == message.channel

            # Waiting for the user to send the options
            options = await self.wait_for('message', check=check)

            # Creating a decision maker object
            decision = DecisionMaker(options.content)

            # Asking if the user wants to add weights
            await message.channel.send(f"Gostaria de adicionar pesos às opções?{os.linesep}Digite 's' para sim e 'n' para não.")

            # Looping until the user enters a valid answer
            while True:
                # Waiting for the user to send the answer
                answer = await self.wait_for('message', check=check)
                # Getting the first letter of the answer
                answer = answer.content.lower()[0]

                if answer == 'n':
                    # If the user doesn't want to add weights
                    await message.channel.send(f"{name} perguntou ao Grande Decison Maker o que fazer.{os.linesep}O Grande Decison Maker diz: ***{decision.make_decision_simple()}***")
                    break

                elif answer == 's':

                    try:
                        # If the user wants to add weights
                        await message.channel.send(f"Esta é a lista de opções que você digitou: {options.content}")
                        await message.channel.send("Digite os pesos separados por vírgulas também(Exemplo: '1, 2, 3'):")
                        # Waiting for the user to send the weights
                        weights = await self.wait_for('message', check=check)
                        # Sending the decision
                        await message.channel.send(f"{name} perguntou ao Grande Decison Maker o que fazer.{os.linesep}O Grande Decison Maker diz: ***{decision.make_decision_weighted(weights.content)}***")
                        break

                    except Exception as e:
                        await message.channel.send(f"Entrada inválida{os.linesep}{e}")
                        await message.channel.send("Digite os pesos separados por vírgulas também(Exemplo: '1, 2, 3'):")
                        # Waiting for the user to send the weights
                        weights = await self.wait_for('message', check=check)
                        # Sending the decision
                        await message.channel.send(f"{name} perguntou ao Grande Decison Maker o que fazer.{os.linesep}O Grande Decison Maker diz: ***{decision.make_decision_weighted(weights.content)}***")
                        break

                else:
                    await message.channel.send("Entrada inválida")

        # Creating !ajuda command
        if message.content.startswith('!ajuda'):
            await message.channel.send(f"""Olá!{os.linesep}Eu sou o Grande Decison Maker, eu fui criado pelo Jonathan Costa para te ajudar a tomar decisões.{os.linesep}{os.linesep}Os comandos são: {os.linesep}***!ola*** - Diz olá para você{os.linesep}***!escolha*** - Inicia o bot{os.linesep}***!ajuda*** - Mostra esta mensagem{os.linesep}{os.linesep}O bot é open source e você pode encontrá-lo aqui:
https://github.com/JonathanFcosta17/Decision_maker""")


# Running the bot
if __name__ == '__main__':
    # Loading the token from the .env file
    load_dotenv()
    TOKEN = os.environ['DISCORD_TOKEN']

    intents = discord.Intents.default()
    intents.message_content = True

    # Creating the bot
    client = MyClient(intents=intents)
    client.run(TOKEN)
