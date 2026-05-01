
import discord
from dotenv import load_dotenv
import os

chat =""

load_dotenv()
token =os.getenv("SECRET_KEY")

import os

from groq import Groq

groq_client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        global chat
        chat += f"{message.author}: {message.content}\n"
        print(f'Message from {message.author}: {message.content}')
        if self.user!= message.author:
            if self.user in message.mentions:
                channel =message.channel


                chat_completion = groq_client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": f"{chat}\nRaaidGPT: ",
                        }
                    ],
                    model="llama-3.3-70b-versatile",
                    )

                messageToSend= chat_completion.choices[0].message.content
                await channel.send(messageToSend)



intents = discord.Intents.default()
intents.message_content= True

discord_client = MyClient(intents=intents)
discord_client.run(token)