A, B, C = map(int, input().split())

num1 = int((A+B) % C)
num2 = int(((A % C) + (B % C))% C)
num3 = int((A * B) % C)
num4 = int(((A % C) * (B % C)) % C)

print(num1)
print(num2)
print(num3)
print(num4)
