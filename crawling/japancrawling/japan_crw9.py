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
import re

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
    

def gglcrawling(driver,age,page):
    if age == 2:
        driver.get("https://colorfully.app/index/models?m=1&agedatas=2,3&page="+str(page))
    else:
        driver.get("https://colorfully.app/index/models?m=1&agedatas="+str(age)+"&page="+str(page))
    time.sleep(2)

    pageString = driver.page_source
    bsObj = BeautifulSoup(pageString, "lxml")
                                                    
    imglist = driver.find_elements(by=By.XPATH, value='''/html/body/div[2]/div[1]/ul[1]/li/a''')

    urllist = []
    for img in imglist:
        urllist.append(img.get_attribute('href'))

    for url in urllist:
        namee = driver.find_elements(by=By.XPATH, value="""//*[@id="link-model4078"]/div/h3/span""")
        if os.path.isdir('img/namee'):
            continue
        url = url.replace('detail','photo')
        driver.get(url)
        time.sleep(1)
        
        try:
        #name 일본어
            name = driver.find_element(by=By.XPATH, value="""/html/body/div[3]/div[1]/div/article/div[2]/h3""").text

            imgs = driver.find_elements(by=By.XPATH, value="""/html/body/div[3]/div[1]/div/div/div/div/a/img""")
            
            name = name.replace(' ','_',1)
            name = name.replace('　','_',1)
            name = name.replace(' ','')
            name = name.replace('　','')
        except:
            continue
        
        try: 
            os.mkdir('/data/notebook/Japancrw/img/'+name)
        except:
            continue
#             os.mkdir('/data/notebook/Japancrw/img/'+name+'1')
#             name = name+'1'
#             print(name)

        picnum=0
    
        if imgs == []:
            os.rmdir('/data/notebook/Japancrw/img/'+name)
            continue
            
        for img in imgs:
            img = img.get_attribute('src')
            image = url_to_image(img)

            if image != "false":
                cv2.imwrite('/data/notebook/Japancrw/img/'+name+'/'+str(picnum)+'.jpg',image)
                picnum+=1
            else:
                print(image)
        if age == 1:
            ag = "10-20"
        elif age == 2:
            ag = "20-30"
        else:
            ag = str(age*10-10)+"-"+str(age*10)
        data = {
                    'name' : name,
                    'age' : ag,
                    'gender' : "female"
                }
        with open('/data/notebook/Japancrw/img/'+name+'/'+name+'.json', 'w') as f:
             f.write(json.dumps(data))
    driver.close()
    