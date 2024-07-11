# 클래스
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

my_dog = Dog("Buddy", 3)
print(my_dog.name)
print(my_dog.bark())


# 상속
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


# 다형성 -> 동일한 인터페이스로 서로 다른 데이터 타입 객체를 다룰 수 있다
animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    print(f"{animal.name} says {animal.speak()}")


# 매직 메서드 (Magic Methods) -> 파이썬이 내부적으로 사용하는 메서드
'''
__init__ : 객체 초기화 메서드
__str__ : 객체의 문자열 표현 반환 (사용자 친화적인 출력)
__repr__ : 객체의 '공식' 문자열 표현을 반환 (객체의 명확한 식별 및 재생성을 위한 출력)

__str__ 와 __repr__의 우선순위
=> 먼저 __str__이 정의되어 있는지 확인하고, 정의되어 있지 않다면 __repr__을 사용
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book({self.title}, {self.author})"

my_book = Book("1984", "George Orwell")
print(str(my_book))
print(repr(my_book))



# 연산자 오버로딩 -> 파이썬 기본 연산자를 사용자 정의 클래스에서 사용할 수 있도록 메서드 정의
"""
__add__: + 연산자
__sub__: - 연산자
__mul__: * 연산자
__truediv__: / 연산자
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)       # self는 왼쪽 피연산자를, other는 오른쪽 피연산자를 나타냄
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(5, 7)
# v1 + v2는 __add__ 메서드를 호출하여 (2 + 5, 3 + 7) 좌표를 가지는 새로운 Vector 객체를 반환
v3 = v1 + v2
print(v3)