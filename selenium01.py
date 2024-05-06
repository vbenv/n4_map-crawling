from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)



# 웹페이지 해당 주소 이동
# driver.get("https://www.naver.com")
res = requests.get("http://google.com")
res.raise_for_status()
print("웹 스크래핑을 진행합니다.")
if res.status_code == requests.codes.ok: #200
    print("웹페이지가 정상이고 정보를 올바르게 받아왔습니다.")
else:
    print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")