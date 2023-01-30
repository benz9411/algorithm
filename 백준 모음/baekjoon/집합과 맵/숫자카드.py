from collections import Counter
N=int(input())
n_lis=list(map(int,input().split()))
M=int(input())
m_lis=list(map(int,input().split()))

n=Counter(n_lis) #이거를 이용해서 비교해함




for i in m_lis:
    if i in n.keys():
        print(n[i],end=' ')
    else:
        print(0,end=' ')

# 주어지는 숫자가 존나 크면 두가지를 생각해야한다
# 이분탐색이나 해쉬구조로 푸는 문제냐
# 탐색이면 이분탐색 이런건 해쉬구조가 좋다고 생각한다.

            

            