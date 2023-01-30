#탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정이다

#stack 구조 구현하기

stack = []

stack.append(5)
stack.append(5)
stack.append(3)
stack.pop()
stack.append(4)
stack.append(7)

print(stack)
print(stack[::-1])