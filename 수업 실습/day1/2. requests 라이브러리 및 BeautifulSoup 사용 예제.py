import requests
from bs4 import BeautifulSoup

url = 'https://ko.wikipedia.org/wiki/위키백과:대문'
response = requests.get(url)

# 요청 성공 여부 확인
if response.status_code == 200:
    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(response.content, 'html.parser')
    # 페이지 제목 추출
    title = soup.find('h1', id='firstHeading').text
    print(f"Title: {title}")
    # 첫 번째 단락 추출
    first_paragraph = soup.find('p').text
    print(f"First paragraph: {first_paragraph}")
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")
