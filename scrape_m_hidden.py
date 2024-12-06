# In this framework I have two files scrape.py and scrape_multiple.py but i have to hide my api key and hash id
# I will install dot env in the terminal (pip3 install python-dotenv) 
# Then I will create a .env file to store my api keys and hash which i wont upload in git.
# we will import the dot env
# to call the api we have to import os


from dotenv import load_dotenv
import pandas as pd
from telethon.sync import TelegramClient
from datetime import datetime
import asyncio
import os

SESSION_NAME = 'telegram_scraper_session'

load_dotenv()


api_id = os.getenv('api_id') 
api_hash = os.getenv('api_hash')
async def scrape_channel_messages(client, channel_name, limit=500):
    """
    Scrape messages from a specific Telegram channel.
    """
    messages = await client.get_messages(channel_name, limit=limit)
    data = []
    for message in messages:
        data.append({
            'Date': message.date,
            'Sender': message.sender_id,
            'Message': message.message
        })
    return pd.DataFrame(data)

def save_to_csv(dataframe, filename):
    """
    Save the scraped data to a CSV file.
    """
    dataframe.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

async def scrape_multiple_channels(client, channels, limit=500):
    """
    Scrape messages from multiple Telegram channels.
    """
    tasks = []
    for channel_name in channels:
        print(f"Starting to scrape channel: {channel_name}")
        tasks.append(scrape_channel_messages(client, channel_name, limit))
    
    results = await asyncio.gather(*tasks)
    
    for channel_name, df in zip(channels, results):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"telegram_messages_{channel_name}_{timestamp}.csv"
        save_to_csv(df, filename)

async def main():

    channels = [
        'the_trading_advisor_stock',
        'STOCKGAINERSS', 
        'TheWealthMagnet',  
        'originalbullbull' 
    ]


    async with TelegramClient(SESSION_NAME, api_id, api_hash) as client:
        print("Connected to Telegram")
        
        await scrape_multiple_channels(client, channels, limit=1000)

if __name__ == '__main__':
    asyncio.run(main())
