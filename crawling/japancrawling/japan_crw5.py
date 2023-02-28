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
    

def gglcrawling(driver,age,gender):
    #2 : male    #1 : female
    #age = 1~8
    driver.get("https://imagenavi.jp/search/#!/cat:5110"+str(gender)+"/"+str(age)+"0%E4%BB%A3/1%E4%BA%BA/%E9%A1%94%E3%81%A4%E3%81%8D/-%E3%82%A4%E3%83%A9%E3%82%B9%E3%83%88%E3%83%87%E3%83%BC%E3%82%BF")

    time.sleep(3)

    pageString = driver.page_source
    bsObj = BeautifulSoup(pageString, "lxml")
    
    imglist = driver.find_elements(by=By.XPATH, value='''//*[@id="intabs-1"]/form/div/div/span/div/a/div/div[1]/div/a''')

    urllist = []
    for img in imglist:
        urllist.append(img.get_attribute('href'))
    for url in urllist:
        try:
            driver.get(url)
            time.sleep(1)
        except:
            continue
        name = url[-8:]

        driver.switch_to.frame(2)
        imgs = driver.find_elements(by=By.XPATH, value="""//*[@id="simthumbArea"]/div/div/div/a/img""")
        
        picnum=0

        try: 
            os.mkdir('/data/notebook/Japancrw/japanimg/low_quality/'+name)
        except:
            continue
#             os.mkdir('/data/notebook/Japancrw/img/'+name+'1')
#             name = name+'1'
#             print(name)
            
        for img in imgs:
            imgurl = img.get_attribute('src')
            
            image = url_to_image(imgurl)
            
            if image != "false":
                try:
                    cv2.imwrite('/data/notebook/Japancrw/japanimg/low_quality/'+name+'/'+str(picnum)+'.jpg',image)
                    picnum+=1
                except:
                    continue
            else:
                print(image)     
        if gender == 2:
            sex = "male"
        else:
            sex = "female"
        data = {
                    'name' : name,
                    'age' : str(age*10)+'-'+str(age*10+10),
                    'gender' : sex
                }
        with open('/data/notebook/Japancrw/japanimg/low_quality/'+name+'/'+name+'.json', 'w') as f:
             f.write(json.dumps(data))
    driver.close()
    
