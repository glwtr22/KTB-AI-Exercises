try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다:", e)


try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError as e:
    print("파일을 찾을 수 없습니다:", e)
finally:
    file.close()


def check_positive(number):
    if number < 0:
        raise ValueError("음수는 허용되지 않습니다")

try:
    check_positive(-5)
except ValueError as e:
    print(e)


class NegativeNumberError(Exception):
    def __init__(self, message="음수는 허용되지 않습니다."):
        self.message = message
        super().__init__(self.message)

def check_positive(number):
    if number < 0:
        raise NegativeNumberError()

try:
    check_positive(-5)
except NegativeNumberError as e:
    print(e)