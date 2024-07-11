# 리스트 컴프리헨션 예제
# 기본 리스트 컴프리헨션
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x*2 for x in numbers]
print("제곱된 숫자들:", squared_numbers)

# 조건을 포함한 리스트 컴프리헨션
even_numbers = [x for x in numbers if x % 2 == 0]
print("짝수들:", even_numbers)



# 딕셔너리 컴프리헨션 예제
numbers = [1, 2, 3, 4, 5]

squared_dict = {x: x*2 for x in numbers}
print("제곱된 딕셔너리:", squared_dict)



# 집합 컴프리헨션 예제
numbers = [1, 2, 3, 4, 5]

squared_set = {x*2 for x in numbers}

print("제곱된 집합:", squared_set)



# 중첩 리스트 컴프리헨션 예제
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened = [num for row in matrix for num in row]
print("Flattened List:", flattened)