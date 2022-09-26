a = int(input("시작 수를 입력해주세요: "))
b = int(input("끝 수를 입력해주세요: "))

for i in range(a, b + 1):

    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end =" ")



