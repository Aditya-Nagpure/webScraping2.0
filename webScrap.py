from bs4 import BeautifulSoup
import requests

url ='https://www.amazon.in/OnePlus-Wireless-Earbuds-Titanium-Playback/dp/B0BYJ6ZMTS/ref=sr_1_5?crid=2MKACHPERY2OA&dib=eyJ2IjoiMSJ9.8bsQBwW9gD2x8Y7pDjqr5u1ri3XqPvITBeM53aQbQUnPmvE9Jmfjb4gzrpdycLEHg1RjnAzpcGQ_V9e6twmQOK36VFCGGLSijbNKRm906nMywgVZn7aPqd8GBoqAxALYmEGSg6M-xGpwMvSvqCouK6Xx2qadG-p-RdrEaZmevhqxEi4BpaJmzmtAidvaxvEIwFF7agI5iMo_sSdMMrlvRotHusVkGrvfVyM6xSrw23g.q99IddNJb-9x6J1jWRNvl40sI_lkMDA3F8hwSgsemz4&dib_tag=se&keywords=oneplus%2Bearbuds&qid=1721759378&sprefix=oneplus%2Bearbuds%2Caps%2C261&sr=8-5&th=1'

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip',
'DNT' : '1', # Do Not Track Request Header
'Connection' : 'close'
}

setPrice= 2200

def toCheckPrice():
    page=requests.get(url, headers=headers)
    soup= BeautifulSoup(page.content, 'html.parser')

    title=soup.find(id='productTitle').get_text()
    product_title=str(title)
    product_title=product_title.strip()
    
    print(product_title)

toCheckPrice()    


