#!/usr/bin/env python
# coding: utf-8

# In[84]:


import pandas as pd # 표 형식의 데이터를 다룰 수 있는 pandas를 pd라고 줄여서 불러옵니다
from selenium import webdriver # 크롬 창을 조종하기 위한 모듈입니다
from selenium.webdriver.common.by import By # 웹사이트의 구성요소를 선택하기 위해 By 모듈을 불려옵니다
from selenium.webdriver.chrome.options import Options # 크롬에서 크롤링을 하기 위해, 웹 드라이버를 설치하는 모듈입니다
import time # 정해진 시간만큼 기다리게 하기 위한 패키지입니다
from selenium.webdriver.common.keys import Keys # 엔터키 입력하는 키
from bs4 import BeautifulSoup
import requests

# The way : 1. 페이지 들어감 -> 검색창 누르기 -> 검색
# 2. 주소 자체에 검색어 넣기

# 주소를 받는 리스트와 크롤링 할 주소 설정
address = []
srch_text = "전기차충전소"
url = 'https://map.naver.com/p/search/' # 검색할 기본 주소
# url2 = url+ srch_text
# srch = requests.get(url2)

# 크롬 꺼지는 현상 방지
options = Options()
options.add_experimental_option("detach", True)

#드라이브 설치 및 불러오기
driver = webdriver.Chrome(options=options)

driver.get(url) # url 실행하는 메소드
time.sleep(3)

# 검색창을 찾아 전기차충전소 입력
query = driver.find_element(By.CLASS_NAME,"input_search")
query.send_keys("전기차충전소")

# 엔터키 입력
query.send_keys(Keys.ENTER)
time.sleep(2)

#iframe 요소 내 주소명 받아오기 때문에 iframe요소로 변경
driver.switch_to.frame("searchIframe")

# 상위 10개 충전소의 이름 받아오기
con2 = driver.find_elements(By.CLASS_NAME,'AFbti')
for i in con2:
    print(i.text)

