#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 09:13:10 2022

@author: parksangbeomm
"""

import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
import pyperclip
import threading

def check_func():
    global init_count, words, pre_words
    
    announcement = driver.find_element_by_id("td_box22")
    announcement.click()
    time.sleep(1)
    new = driver.find_element_by_xpath('//*[@id="tr_box_22"]/table/tbody/tr[1]/td[1]/div/a')
    s = new.text
    if init_count==0:
        words,pre_words = s,s
    else:
        pre_words = words
        words = s
        if words != pre_words:
            webbrowser.open(url)
            pre_words = words
    driver.refresh()
    time.sleep(1)
    
    init_count += 1
    print((init_count-1)*3, "minute...")
    if(init_count==144):
        driver.quit()
    threading.Timer(180, check_func).start()
    
init_count, login = 0,0
words, pre_words = "", ""

url = 'https://hisnet.handong.edu/'
webdriver_options = webdriver.ChromeOptions()
webdriver_options .add_argument('headless')
# step2. 크롬드라이버로 hisnet 접속
driver = webdriver.Chrome('', options=webdriver_options)


driver.get(url)
driver.switch_to.frame("MainFrame")
time.sleep(1)
# step3. 로그인 버튼을 찾고 클릭

# 3-1. id, pw 입력할 곳 찾기
tag_id = driver.find_element_by_name('id')
tag_pw = driver.find_element_by_name('password')
tag_id.clear()

# 3-2. id 입력
uid = ""
tag_id.click()
pyperclip.copy(uid)
tag_id.send_keys(Keys.COMMAND, 'v')
time.sleep(0.5)

# 3-3. pw 입력
upw = ""
tag_pw.click()
pyperclip.copy(upw)
tag_pw.send_keys(Keys.COMMAND, 'v')
time.sleep(0.5)

# 3-4. 로그인 버튼을 클릭
login_btn = driver.find_element_by_xpath(
    "//*[@id='loginBoxBg']/table[2]/tbody/tr/td[5]/form/table/tbody/tr[3]/td/table/tbody/tr/td[2]/input")
login_btn.click()
time.sleep(1)
print("login success")

# TODO: 3-5-2. (로그인 성공했을 경우) 코로나 체크 떳을 경우 - 체크
if len(driver.find_elements_by_xpath("/html/body/div[3]/div/button")) > 0:
    announce_btn = driver.find_element_by_xpath("/html/body/div[3]/div/button")
    time.sleep(3)
    announce_btn.click()
# TODO: "좋은하루되세요" alert창 처리
    try:
        Alert(driver).accept()
    except:
        print("no alert")
print("function start")
check_func()
