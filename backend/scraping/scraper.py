from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time
import json

# Path to ChromeDriver
chrome_path = "/opt/homebrew/bin/chromedriver"
service = Service(chrome_path)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

# 데이터 저장 경로 설정
raw_data_path = "data/raw_data.json"
processed_data_path = "data/processed_data.csv"

# 실시간 베스트 갤러리에서 게시글 목록 가져오기
BASE_URL = "https://gall.dcinside.com"
LIST_URL = f"{BASE_URL}/board/lists?id=dcbest"

driver.get(LIST_URL)
time.sleep(2)

soup = BeautifulSoup(driver.page_source, "html.parser")
post_links = []

# 게시글 목록 가져오기
for post in soup.select("tr.ub-content td.gall_tit a:nth-child(1)"):
    href = post["href"]
    post_links.append(BASE_URL + href)

print(f"총 {len(post_links)}개의 게시글을 찾았습니다.")

# 각 게시글에서 데이터 크롤링
comments_data = []

for post_url in post_links[:5]: # 상위 5개 게시물만 크롤링 (속도 문제 이슈)
    driver.get(post_url)
    time.sleep

# 데이터 저장

# 드라이버 종료