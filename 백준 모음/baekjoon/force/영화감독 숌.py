# 종말의 숫자 즉 '666'처럼 6이 3개이상 연속 !!
# n번쨰로 작은 종말 숫자!!

n = int(input())
a = 666
cnt = 0

while n:
    if "666" in str(a):
        n -= 1
    a += 1

print(a-1)