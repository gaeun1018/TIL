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
import os.path as osp
from multiprocessing import Process, Queue

from PyQt5.QtWidgets import *
import time
from selenium.webdriver.common.action_chains import ActionChains
import os
import csv

import numpy as np
from urllib.request import Request, urlopen
from urllib.request import urlopen, Request
from urllib.parse import urlencode, quote_plus

from face_detect import detection
import warnings

warnings.filterwarnings(action='ignore')

import argparse
from argparse import ArgumentParser, Namespace

def url_to_image(url, readFlag=cv2.IMREAD_COLOR):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
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
    try:
        content = page.read()
    except:
        return "false"

    image = np.asarray(bytearray(content), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def gglcrawling(keyword,driver):
    driver.get("https://www.google.co.kr/imghp?hl=ko&authuser=0&ogbl")##open google image search page

    time.sleep(2)
    driver.find_element(by=By.CSS_SELECTOR, value="input.gLFyf").send_keys(keyword)
    driver.find_element(by=By.CSS_SELECTOR, value="input.gLFyf").send_keys(Keys.RETURN)

    time.sleep(2)

    last_height = driver.execute_script("return document.body.scrollHeight") #initialize standard of height first

    while True: #break가 일어날 때 까지 계속 반복
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #페이지 스크롤 시키기

        time.sleep(1)

        new_height = driver.execute_script("return document.body.scrollHeight") ## update new_height
        if new_height == last_height:#이전 스크롤 길이와 현재의 스크롤 길이를 비교
            try:
                driver.find_element(by=By.CSS_SELECTOR, value=".mye4qd").click()
#                 driver.find_element_by_css_selector(".mye4qd").click() ## click more button 더보기 버튼이 있을 경우 클릭
            except:
                break # 더보기 버튼이 없을 경우는 더 이상 나올 정보가 없다는 의미이므로 반복문을 break
        last_height = new_height ##last_height update



    pageString = driver.page_source
    bsObj = BeautifulSoup(pageString, "lxml")

    imglist = driver.find_elements(by=By.CSS_SELECTOR, value="img.rg_i.Q4LuWd")
    return imglist


    driver.close()
    
def imagecrawling(que1,keyword,driver):

    imglist = gglcrawling(keyword,driver)
    for img in imglist:
        ActionChains(driver).click(img).perform()
        time.sleep(1)
        try:
            imgurl = driver.find_element_by_xpath('''//*[@id="Sva75c"]/div/div/div/div[3]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img''').get_attribute("src")
            que1.put(imgurl)
        except:
            pass
    que1.put(0)
    
def main(args):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--disable-dev-shm-usage")
    path= args.driver
    driver = webdriver.Chrome(path, options=chrome_options)
    
    file = open(args.csv,'r')
    f = csv.reader(file)
    lists = []
    for i in f:
        lists.append(i[0])
    per=0
    while True:
        num=0
        try:
            keyword = lists[per+1]
        except:
            break
        if per%50==0:
            print(per)
        que1 = Queue()
        proc1 = Process(target = imagecrawling, args=(que1, keyword, driver))
        ######
        try:
            os.mkdir(osp.join(args.output, 'a'+str(per).zfill(6)))
        except:
            per+=1
            continue
        ######
        proc1.start()
        
        compare = [512,]
        combool = False
        false = 0
        while True:
            if false>30:
                per+=1
                break
            img = que1.get()
            if img==0:
                per+=1
                break
            img = url_to_image(img)
            if img == "false":
                continue
            result = detection(img,compare,combool)
            time.sleep(1)
            if result != "False":
                if num==0:
                    compare = result
                    combool = True
                    result = detection(img,compare,combool)
                cv2.imwrite(osp.join(osp.join(args.output, 'a'+str(per).zfill(6)),'save_insta_image'+str(num)+'.png'), result[0].aimg)
                num +=1
                false = 0
            else:
                false+=1
                
            if num == args.crawlnum:
                per+=1
                break
        proc1.terminate()
        proc1.join()
    driver.close()
    
if __name__ == '__main__': 
    parser = argparse.ArgumentParser(description='google crawling')
    
    parser.add_argument('--driver', default='', type=str, help='Path to Chrome driver')
    parser.add_argument('--csv', default='', type=str, help='csv file with the name you want to crawl')
    parser.add_argument('--output', default='', type=str, help='Path where the crawled image will be stored')
    parser.add_argument('--crawlnum', default='', type=int, help='Maximum number of crawls per name')


    args = parser.parse_args()
    main(args)