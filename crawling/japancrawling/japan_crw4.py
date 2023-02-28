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
    

def gglcrawling(driver,age,male):
    sex = ["%E7%94%B7%","%E5%A5%B3%"]
            #0 : male    #1 : female
#     for age in range(3,8):
#         for male in range(1,2):
    driver.get("https://www.horipro.co.jp/talent-search/?search_flag=attribute&sex%5B%5D="+sex[male]+"E6%80%A7&min-age="+str(age*10)+"&max-age="+str(age*10+9))

    time.sleep(3)

    pageString = driver.page_source
    bsObj = BeautifulSoup(pageString, "lxml")

    imglist = driver.find_elements(by=By.XPATH, value='''/html/body/div[1]/div/section/div/div[1]/section/section/ul/li/div/div/a''')

    urllist = []
    for img in imglist:
        urllist.append(img.get_attribute('href'))
    for url in urllist:
        try:
            driver.get(url)
            time.sleep(1)
        except:
            continue
        if "international" in url:
            try:
                name = driver.find_element(by=By.XPATH, value="""//*[@id="profile"]/div[1]/div/div/div/div[1]/p[3]""").text

                name = name.replace(' ','_',1)
                name = name.replace('　','_',1)
                name = name.replace(' ','')
                name = name.replace('　','')

                imgs = driver.find_elements(by=By.XPATH, value="""//*[@id="profile"]/div[1]/div/p/img""")
            except:
                continue
        elif "horipro.co.jp" in url:
            name = url[26:]

            imgs = driver.find_elements(by=By.XPATH, value="""/html/body/div[1]/div[3]/div[1]/div/div[1]/ul[2]/li/dl/dd/img""")

        picnum=0

        try: 
            os.mkdir('/data/notebook/Japancrw/img/'+name)
        except:
#             continue
            os.mkdir('/data/notebook/Japancrw/img/'+name+'1')
            name = name+'1'
            print(name)

        for img in imgs:
            imgurl = img.get_attribute('src')
            try:
                image = url_to_image(imgurl)
            except:
                continue
            if image != "false":
                try:
                    cv2.imwrite('/data/notebook/Japancrw/img/'+name+'/'+str(picnum)+'.jpg',image)
                    picnum+=1
                except:
                    continue
            else:
                print(image)     
        if male == 0:
            sex = "male"
        else:
            sex = "female"
        data = {
                    'name' : name,
                    'age' : str(age*10)+'-'+str(age*10+10),
                    'gender' : sex
                }
        with open('/data/notebook/Japancrw/img/'+name+'/'+name+'.json', 'w') as f:
             f.write(json.dumps(data))
    driver.close()
    
