import requests
from bs4 import BeautifulSoup
import os

# CONFIG
TARGET_BUY_PRICE = 3500 
SYSTEM_NAME = "Sol" # Change to your home system
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

def check_elite_silver():
    # We use Inara's search URL for Silver (Commodity ID 46)
    url = f"https://inara.cz/elite/commodity/46/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Logic to find the 'Min Buy Price' on the page
    # Note: Inara's HTML changes, so this is a simplified example
    try:
        price_text = soup.find(text="Min buy price").find_next('span').text
        current_price = int(price_text.replace(' Cr', '').replace(',', ''))
        
        if current_price <= TARGET_BUY_PRICE:
            msg = f"🚀 CMDR, Silver is cheap at {current_price} Cr! Check Inara for the station."
            requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}")
    except:
        print("Could not parse Inara data. Check your scraper logic.")

if __name__ == "__main__":
    check_elite_silver()
