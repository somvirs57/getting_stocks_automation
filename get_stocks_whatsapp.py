# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 12:05:37 2020

@author: somvi
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from twilio.rest import Client   #pip install twilio


def get_price():
    path = r'C:\Program Files (x86)\chromedriver.exe' #excutable path for chromedriver

    url = 'https://in.finance.yahoo.com/' 
    
    topic = "Idea.NS"    
    
    #options to use the chrome browser in background
    #op = webdriver.ChromeOptions()   
    #op.add_argument('headless')
    #driver = webdriver.Chrome(executable_path=path, options=op)
    driver = webdriver.Chrome(path)
    
    driver.get(url)

    search_box = driver.find_element_by_id('yfin-usr-qry')
    # we use try and except in case of wrong search query or any other exception
    try:
        search_box.send_keys(topic)       #put search query in box
        time.sleep(5)
        search_box.send_keys(Keys.ENTER)  # press enter button  
        print(driver.current_url)
        time.sleep(5)
     
        classes = driver.find_element_by_id("quote-header-info") #get the div for stock info
        price_span = classes.find_elements_by_tag_name("span")   #get span for prive value
        
        price = price_span[3].text 
        
        time.sleep(5)
        
        return price
        
    except:
        print('An error occured')
        
    finally:
        driver.close()
        
def send_message(msg):
    client = Client(username='*****', password='**********',
                account_sid='*********')
    from_number = 'whatsapp:*******'
    to_number = 'whatsapp:*********'
    
    client.messages.create(body=msg, from_=from_number, to=to_number)
    print('successfull')
        
if __name__ == "__main__":
    price = float(get_price())
    print(f'{price} is the current price')
    
    upper_limit = float(20.00)
    lower_limit = float(07.00)
    
    
    if price>upper_limit:
        msg = "sell the stocks for benefit as it is " + str(price)
    elif price<lower_limit:
        msg = 'sell the stocks or you will be in loss as it is ' + str(price)
    else:
        msg = 'price is between the desired range i.e ' + str(price)   
        
        
    send_message(msg)
    
    
    
    
    
    