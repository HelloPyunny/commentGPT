from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# ChromeDriver 경로
chrome_path = "/opt/homebrew/bin/chromedriver"
service = Service(chrome_path)

# Chrome 옵션 설정
options = Options()
options.add_argument("--headless")  # 브라우저 창 없이 실행
options.add_argument("--disable-gpu")  # GPU 비활성화
options.add_argument("--no-sandbox")  # 보안 샌드박스 비활성화 (Linux에서 필요할 수 있음)

# WebDriver 초기화
driver = webdriver.Chrome(service=service, options=options)

# WebDriver 테스트
driver.get("https://www.google.com")
print(driver.title)  # "Google" 출력
driver.quit()
