# 함수
def great(name):
    return f"Hello, {name}!"
'''
def 함수이름(매개변수):
    코드 블록
    return 반환값
'''

result = great("Bob")
print(result)

# lambda 함수
square = lambda x : x ** 2
print(square(5))

# map 함수의 인자로 사용
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x : x ** 2, numbers))
print(squares)

# 가변 인자 (*args) : 값 개수에 상관 없이, 전부 인자로 받아줌
def add(*args):
    return sum(args)

print(add(1, 2, 3, 4))

# 키워드 가변인자 (**kwargs)
def introduce(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

introduce(name='Alice', age=30, city="Seoul")       # key = value 값으로 구성된 가변인자

# map, filter, reduce 함수
# map 함수, 모든 요소에 함수를 적용하여 새로운 리스트 반환
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

# filter 함수, 조건에 맞는 요소만 걸러내어 새로운 리스트 반환
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x:x%2==0, numbers))
print(evens)

# reduce 함수, 모든 요소를 누적하여 단일 값을 반환
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y : x * y, numbers)       # 1 * 2 * 3 * 4 = 24 반환
print(product)