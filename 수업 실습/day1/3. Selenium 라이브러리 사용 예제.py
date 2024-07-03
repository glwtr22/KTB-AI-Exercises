from selenium import webdriver
from selenium.webdriver.common.by import By

# URL 설정
URL = "https://ko.wikipedia.org/wiki/위키백과:대문"

# Chrome 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument("--headless")                  # 브라우저 창을 띄우지 않고 백그라운드 실행 -> 웹 스크래핑, 자동화 시스템에서 자주 사용, UI 필요 X 인 경우 유용
options.add_argument('--disable-dev-shm-usage')     # 공유 메모리 사용 비활성화
options.add_argument("--no-sandbox")                # Chrome이 sandbox 모드에서 실행되지 않도록 설정

# 앞서 설정한 ChromeOptions 객체 전달을 통해, 웹 드라이버 설정
driver = webdriver.Chrome(options=options)

# 예외 처리
try:
    # 위키백과 대문 페이지 열기
    driver.get(URL)

    # "우리 모두가 만들어가는 자유 백과사전"과 "문서 이하 내용" 추출
    main_content = driver.find_element(By.CSS_SELECTOR, "#mw-content-text > div.mw-content-ltr.mw-parser-output > div.main-box.main-top > div > p:nth-child(2)").text
    print("Main Content:", main_content)
finally:        # try 블록 끝나면 실행
    # 웹 드라이버 종료
    driver.quit()

'''
웹 드라이버란?
웹 브라우저를 제어하는 프로그램이나 라이브러리
주로 자동화된 웹 테스트나 웹 스크래핑 등의 작업에서 사용된다
Ex) Selenium
'''