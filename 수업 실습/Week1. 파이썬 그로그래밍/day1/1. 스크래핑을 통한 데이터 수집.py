import requests
from bs4 import BeautifulSoup

url = 'https://www.aihub.or.kr/'

# 웹 페이지 요청
response = requests.get(url)
# 요청 성공 여부 확인
response.raise_for_status()

# BeautifulSoup 객체 생성
soup = BeautifulSoup(response.content, 'html.parser')
'''
BeautifulSoup 라이브러리를 사용해 HTML 콘텐츠 파싱
=> HTML 문서를 쉽게 탐색하고 필요한 데이터 추출 가능
'''

# 인기 데이터 Top 3 섹션 찾기
top3_section = soup.find('div', class_='secR')
'''
div 태그를 찾고, 해당 태그의 클래스 속성값이 'secR'인 첫 번쨰 요소 찾기
=> <div class='secR"> ... </div> 찾아줌
'''

# 각 데이터 항목 추출
data_list = top3_section.find_all('div', class_='list')
'''
<div class="secR">
    <div class="list">Item 1</div>
    <div class="list">Item 2</div>
    <div class="list">Item 3</div>
</div>
인 경우에 ...
=> [<div class="list">Item 1</div>, <div class="list">Item 2</div>, <div class="list">Item 3</div>]
추출
'''

# 데이터 제목 추출
titles = []
for data in data_list:
    title = data.find('h3').get_text(strip=True)    # strip=True : 앞뒤 공백 제거
    clean_title = title.split(']')[-1].strip()      # ']'를 기준으로 텍스트 분리 후, 마지막 요소 선택
    titles.append(clean_title)

# 추출한 데이터 출력
for idx, title in enumerate(titles, start=1):
    print(f"TOP {idx}: {title}")