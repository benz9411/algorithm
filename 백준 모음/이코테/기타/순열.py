#서로 다른 l개의 알파벳

from itertools import combinations


L,C=map(int,input().split())
arr=input().split(' ')
arr.sort()
#문제 요구: 최소 한개의 모음과 최소 두개의 자음으로 구성되어 있다.

vowels=('a','e','i','o','u')

for passward in combinations(arr,L):
    count=0
    for i in passward:
        if i in vowels:
            count+=1
    if count>= 1 and count<=L-2: #최소 1개의 모음과 최소 2개의 자음이 있는 경우만
        print("".join(passward))





