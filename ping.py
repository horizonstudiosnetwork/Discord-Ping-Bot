import discord
import asyncio
import requests

# Replace 'YOUR_WEBHOOK_URL' with your actual webhook URL
WEBHOOK_URL = 'YOUR_WEBHOOK_URL'

# Function to send a message to Discord webhook
async def send_webhook_message(message):
    data = {
        'content': message
    }
    await asyncio.to_thread(requests.post, WEBHOOK_URL, json=data)

# Function to continuously ping @everyone
async def ping_everyone():
    while True:
        message = '@everyone https://discord.gg/Wp7TWvAhH7'
        await send_webhook_message(message)
        await asyncio.sleep(0.1)  # Wait for 0.5 seconds before sending the next ping

# Define intents
intents = discord.Intents.default()

# Create a Discord client with intents
client = discord.Client(intents=intents)

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    # Start pinging @everyone
    await ping_everyone()

# Run the bot
client.run('Your_Bot_Token')
