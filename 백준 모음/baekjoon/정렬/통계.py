from collections import Counter
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
    
# 1.산술평균 첫째자리 반올림
arg=sum(arr)/n
print(f'{arg:.0f}')
#중앙값
middle=sorted(arr)
if n%2==0:
    print(middle[(n//2)-1]+middle[n//2])
else:
    print(middle[n//2])

#최빈값
a=Counter(middle)
order=a.most_common()
maximum = order[0][1] #첫번째 최빈값을 개수를 넣어줌

modes=[]
for num in order:
    if num[1] == maximum:
        modes.append(num[0])
if len(modes)==1:
    print(modes[0])
else:
    print(modes[1])

#범위
print(abs(middle[0])+abs(middle[-1]))
