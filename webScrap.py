import os
from bs4 import BeautifulSoup
import requests
import smtplib
from email.message import EmailMessage
from threading import Timer

url = 'https://www.amazon.in/OnePlus-Wireless-Earbuds-Titanium-Playback/dp/B0BYJ6ZMTS/ref=sr_1_5?crid=2MKACHPERY2OA&dib=eyJ2IjoiMSJ9.8bsQBwW9gD2x8Y7pDjqr5u1ri3XqPvITBeM53aQbQUnPmvE9Jmfjb4gzrpdycLEHg1RjnAzpcGQ_V9e6twmQOK36VFCGGLSijbNKRm906nMywgVZn7aPqd8GBoqAxALYmEGSg6M-xGpwMvSvqCouK6Xx2qadG-p-RdrEaZmevhqxEi4BpaJmzmtAidvaxvEIwFF7agI5iMo_sSdMMrlvRotHusVkGrvfVyM6xSrw23g.q99IddNJb-9x6J1jWRNvl40sI_lkMDA3F8hwSgsemz4&dib_tag=se&keywords=oneplus%2Bearbuds&qid=1721759378&sprefix=oneplus%2Bearbuds%2Caps%2C261&sr=8-5&th=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip',
    'DNT': '1',
    'Connection': 'close'
}

setPrice = 2200

def alert_system(product, link):
    email_id = os.getenv('EMAIL_ID')
    email_pass = os.getenv('EMAIL_PASS')

    if not email_id or not email_pass:
        print("Email ID or password not set in environment variables.")
        return

    print(f"Using email ID: {email_id}") 
    print(f"Using email pass: {email_pass}") 

    msg = EmailMessage()
    msg['Subject'] = 'Price Drop Alert'
    msg['From'] = email_id
    msg['To'] = 'adinagpure.9@gmail.com' 
    msg.set_content(f'Hey, the price of {product} has dropped!\n{link}')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_id, email_pass)
            smtp.send_message(msg)
        print('Email sent successfully.')
    except smtplib.SMTPAuthenticationError as e:
        print(f"Failed to authenticate with SMTP server: {e}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def toCheckPrice():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle')
    if title:
        product_title = title.get_text().strip()
        print(product_title)
    else:
        print("Could not find the product title.")
        return

    price = soup.find('span', {'class': 'a-price-whole'})
    if price:
        product_price = ''
        for i in price.get_text():
            if i.isnumeric() or i == '.':
                product_price += i
        product_price = float(product_price)
        print(product_price)
    else:
        print("Could not find the product price.")
        return

    if product_price <= setPrice:
        alert_system(product_title, url)
        print('Alert sent')
    else:
        print('No alert sent')
    
    Timer(60, toCheckPrice).start()

toCheckPrice()
