# 리스트 예제
# 리스트 생성 및 기본 사용법
fruits = ["apple", "banana", "cherry"]
print("리스트:", fruits)

# 리스트 요소 접근
print("첫 번째 요소:", fruits[0])
print("마지막 요소:", fruits[-1])

# 리스트 요소 변경
fruits[1] = "blueberry"
print("요소 변경 후:", fruits)

# 리스트 요소 추가
fruits.append("date")
print("요소 추가 후:", fruits)

# 리스트 요소 삭제
fruits.remove("apple")
print("요소 삭제 후:", fruits)

# 리스트 길이
print("리스트 길이:", len(fruits))



# 세트 예제
# 세트 생성 및 기본 사용법
fruits = {"apple", "banana", "cherry"}
print("세트 : ", fruits)

# 세트 요소 추가
fruits.add("date")
print("요소 추가 후:", fruits)

# 세트 요소 삭제
fruits.remove("banana")
print("요소 삭제 후:", fruits)

# 세트 길이
print("세트 길이:", len(fruits))

fruits.add("date_1")
print("요소 추가 후:", fruits)



# 딕셔너리 예제
# 딕셔너리 생성 및 기본 사용법
fruit_colors = {"apple":"red", "banana":"yellow", "cherry":"red"}
print("딕셔너리:", fruit_colors)

# 딕셔너리 요소 접근
print("사과의 색:", fruit_colors["apple"])

# 딕셔너리 요소 추가
fruit_colors["date"] = "brown"
print("요소 추가 후:", fruit_colors)

# 딕셔너리 요소 삭제
del fruit_colors["banana"]
print("요소 삭제 후:", fruit_colors)

# 딕셔너리 길이
print("딕셔너리 길이:", len(fruit_colors))



# 튜플 예제
fruits = ("apple", "banana", "cherry")
print("튜플:", fruits)

# 튜플 요소 접근
print("첫 번째 요소:", fruits[0])
print("마지막 요소:", fruits[-1])

# 튜플 언패킹
fruit1, fruit2, fruit3 = fruits
print("언패킹된 요소:", fruit1, fruit2, fruit3)



# collections 모듈 예제
from collections import deque, namedtuple, defaultdict, Counter

# deque
dq = deque(["apple", "banana", "cherry"])
dq.append("date")
dq.popleft()
print("Deque:", dq)

# namedtuple
Fruit = namedtuple('Fruit', 'name color')
apple = Fruit(name="apple", color="red")
print("NamedTuple:", apple)

# defaultdict
dd = defaultdict(int)
dd["apple"] += 1
print("DefaultDict:", dd)

# Counter
cnt = Counter(["apple", "banana", "apple", "cherry", "banana", "banana"])
print("Counter:", cnt)