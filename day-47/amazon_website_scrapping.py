import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os
from pprint import pprint
import lxml

load_dotenv()

URL = 'https://www.amazon.in/Samsung-Inverter-Refrigerator-RT28C3032GS-HL/dp/B0BR3Z729L/ref=sr_1_7?_encoding=UTF8&content-id=amzn1.sym.58c90a12-100b-4a2f-8e15-7c06f1abe2be&dib=eyJ2IjoiMSJ9.WeNO08BDbM9HwjBZfrKHXTPij4UsHuiD5y5ldIu-LovlLfxbQzfxNRS8p5dslkSxnBEV8snQiOljnrsT5WwsD35_zEFl-1MloyNbwJa-uvsDK1-ke4AS8_UWcHdeHeKlKI-bSiIeJO3PogMYGH-IjdoJDSo_eNPGjiM4t-ajv-4J66h5V8hNW12PvhL1tHvYE-vYA5h54YgrmGrppdJkVnUNdca5VlhAGrHANAuge5DxZYsxzNLh7u5u5Tj9SJhc5dyHIX-Pei6VGL55aIOLTjhTHSWKuI4mvTGGW_57Ycs.U4lyIFYQkX1cRrzA2-EARBdy0dukvihlLyAnuA7jZJI&dib_tag=se&pd_rd_r=3ceac98d-1394-4f4d-9777-326d445365c7&pd_rd_w=P3vIi&pd_rd_wg=WiONg&pf_rd_p=58c90a12-100b-4a2f-8e15-7c06f1abe2be&pf_rd_r=FHY4Z9SZ7ASEBDNQWPJJ&qid=1725274856&refinements=p_85%3A10440599031&rps=1&s=kitchen&sr=1-7&th=1'
EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']
BUY_PRICE = 25000
TO_ADDRESS = os.environ['TO_EMAIL']

class Amazon_Site_Products:
    def __init__(self) -> None:
        self.url = URL
        self.my_email = EMAIL
        self.password = PASSWORD
        self.to_address = TO_ADDRESS
        # self.headers = {
        #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        #         "Accept-Encoding": "gzip, deflate, br, zstd",
        #         "Accept-Language": "en-IN,en;q=0.9,hi;q=0.8",
        #         "Dnt": "1",
        #         "Priority": "u=0, i",
        #         "Sec-Ch-Ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
        #         "Sec-Ch-Ua-Mobile": "?0",
        #         "Sec-Ch-Ua-Platform": "\"Windows\"",
        #         "Sec-Fetch-Dest": "document",
        #         "Sec-Fetch-Mode": "navigate",
        #         "Sec-Fetch-Site": "cross-site",
        #         "Sec-Fetch-User": "?1",
        #         "Upgrade-Insecure-Requests": "1",
        #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        # }
        
        self.headers = {
                "Accept-Language": "en-IN,en;q=0.9,hi;q=0.8",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
        }
    
    def get_prices(self):
        response = requests.get(URL, headers=self.headers)
        amazon_website_prod = response.content
        response.raise_for_status()
        soup = BeautifulSoup(amazon_website_prod, 'lxml')
        print(soup.prettify())
        
        price = soup.find(name='span', class_='a-price-whole').get_text()
        self.product_name = soup.find(name='span', id='productTitle').get_text().strip()
        self.product_price = float(price.replace(',',''))
        
        print(self.product_name)
        print(self.product_price)
        return self.product_price
    
    def send_updates(self, current_price):
        self.message = f'Subject:Amazon Price Drop Alert!🤑\n\n{self.product_name} is on sale for the best price: ₹{self.product_price}'.encode('utf-8')
        if current_price < BUY_PRICE:
            try:
                with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                    connection.starttls()
                    connection.login(user=self.my_email,
                                    password=self.password)
                    connection.sendmail(from_addr=self.my_email,
                                        to_addrs=self.to_address,
                                        msg=self.message)
            except Exception as e:
                print(f'Failed to sent the message due to: {e}')