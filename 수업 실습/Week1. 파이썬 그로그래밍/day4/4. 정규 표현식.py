import re

# 이메일 추출
text = "Contact us at support@example.com or sales@example.com"
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9._]+\.[A-Z|a-z]{2,7}\b"
'''
`\b`: 시작과 끝에 각각 위치하여, 이메일 주소 앞뒤에 공백이나 다른 문자들이 올 수 있도록 함
[] 안에 포함된 문자는 허용되는 문자 집합을 정의
`+`: 앞의 문자 집합이 하나 이상 반복됨을 의미
@ : 로컬 파트와 도메인 파트 구분자
`\.` : 도메인 파트의 첫 번째 부분과 최상위 도메인(TLD)을 구분하는 마침표 (. 문자로 인식을 위해 이스케이프 문자 추가한 것)

[A-Z|a-z]{2,7}:
최상위 도메인(TLD)을 정의
[A-Z|a-z]는 대문자와 소문자 알파벳을 허용, |는 논리적 "OR" 연산자
{2,7}는 앞의 문자 집합이 최소 2번에서 최대 7번 반복됨을 의미(TLD는 2자에서 7자 사이)
'''

matches = re.findall(pattern, text)
print("이메일:", matches)



# HTML 태그 제거
html = "<p>This is a <b>bold</b> paragraph.</p>"
pattern = r"<.*?>"
'''
r은 raw string을 의미

<.*?> : 태그 내의 임의의 문자(0개 이상의 문자)를 최소 반복(비탐욕적)으로 매칭
. : 모든 단일 문자 의미(개행 제외)
* : 바로 앞의 패턴이 0번 이상 반복됨을 의미
? : 비탐욕적 수량자 생성

기본적으로 *은 탐욕적으로 동작해 가능한 많은 문자 매칭하려고 함
예를 들어, <p>Text <b>bold</b></p> 문자열에 대해 <.*> 패턴은 <p>Text <b>bold</b></p> 전체를 매칭
but,
*?는 비탐욕적이므로 가능한 최소한의 문자를 매칭(첫 번째 > 문자까지의 최소 문자를 매칭)
'''
clean_text = re.sub(pattern, "", html)
print("태그 제거 후 텍스트:", clean_text)