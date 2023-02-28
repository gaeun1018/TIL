#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#google 고화질 크롤링

from selenium import webdriver
import time
import selenium
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import cv2
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import numpy as np
from urllib.request import Request, urlopen
from urllib.request import urlopen, Request
from urllib.parse import urlencode, quote_plus
import os 
import json
from PIL import Image 
from io import BytesIO
import requests

def url_to_image(url, readFlag=cv2.IMREAD_COLOR):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
#     resp = urllib.request.urlopen(url)


    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

    req = urllib.request.Request(url, headers=hdr)
    try:
        page = urlopen(req)
    except:
        return "false"
#     try:
#         page = urlopen(req)
#     except:
#         print("error")
    try:
        content = page.read()
    except:
        return "false"

    image = np.asarray(bytearray(content), dtype="uint8")
#     image = np.asarray(bytearray(urlopen(resp).read), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image
    
    

def gglcrawling(driver,gender,age):
    if gender == 0:
        gender = "men"
    else:
        gender = "women"

    if age == 3:
        age = "60"
    else:
        age = str(age*20)+'-'+str(age*20+10)

    driver.get("https://stage-model.com/tag/"+gender+age)##open google image search page

    time.sleep(2)

    pageString = driver.page_source
    bsObj = BeautifulSoup(pageString, "lxml")

    # genderlist = driver.find_elements(by=By.CSS_SELECTOR, value='members li')
    imglist = driver.find_elements(by=By.XPATH, value='''//*[@id="wrap"]/main/section/div/ul/li/a''')
    urllist = []

    for img in imglist:
        urllist.append(img.get_attribute('href'))

    for url in urllist:
        driver.get(url)
        time.sleep(1)

        name = driver.find_element(by=By.XPATH, value="""//*[@id="wrap"]/main/div[1]/div/div[1]/div[2]/h2/span""").text
        name = name.replace(' ','_')
        name = name.replace('　','_')

        year = driver.find_element(by=By.XPATH, value="""//*[@id="wrap"]/main/div[1]/div/div[1]/div[2]/div/dl[1]/dd""").text
        age = 2022 - int(year[:4])

        try: 
            os.mkdir('/data/notebook/Japancrw/img/'+name)
        except:
            continue
#             os.mkdir('/data/notebook/Japancrw/img/'+name+'1')
#             name = name+'1'
#             print(name)

        picnum=0
        imgs = driver.find_elements(by=By.XPATH, value="""//*[@id="wrap"]/main/div/div/div[1]/div[1]/ul[1]/div/div/div/div/li/img""")

        for img in imgs:
            img = img.get_attribute('src')
            if 'webp' in img:
                img=Image.open(BytesIO(requests.get(img).content)).convert("RGB")
                img.save('/data/notebook/Japancrw/img/'+name+'/'+str(picnum)+'.jpg')
                picnum+=1
                
            elif 'jpg' in img:
                image = url_to_image(img)

                if image != "false":
                    cv2.imwrite('/data/notebook/Japancrw/img/'+name+'/'+str(picnum)+'.jpg',image)
                    picnum+=1
                else:
                    print(image)
            
            
        if gender == "men":
            sex = "male"
        else:
            sex = "female"
            
        data = {
                    'name' : name,
                    'age' : str(age),
                    'gender' : sex
                }
        with open('/data/notebook/Japancrw/img/'+name+'/'+name+'.json', 'w') as f:
             f.write(json.dumps(data))
    driver.close()
    