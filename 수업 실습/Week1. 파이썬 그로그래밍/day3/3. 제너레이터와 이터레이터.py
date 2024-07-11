# 이터레이터 클래스
class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        # __iter__ 메서드는 이터레이터 객체 자체를 반환해야 함
        return self

    def __next__(self):
        # __next__ 메서드는 다음 값을 반환
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration

counter = Counter(5)

for num in counter:
    print(num)


# 제너레이터 함수
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)

for num in counter:
    print(num)

# yield 키워드 -> 제너레이터 함수에서 값을 반환하고 함수의 실행 상태를 일시 중지
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(next(gen))
print(next(gen))
print(next(gen))