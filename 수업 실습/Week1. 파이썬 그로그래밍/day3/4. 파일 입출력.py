# 파일 쓰기
with open('example.txt', 'w') as file:
    file.write("hello, world")

# 여러 줄 쓰기
lines = ['First line\n', 'Second line\n', 'Third line\n']
with open('example.txt', 'w') as file:
    file.writelines(lines)



# 파일 읽기
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# 파일 한 줄씩 읽기
with open('example.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()
        print("*")