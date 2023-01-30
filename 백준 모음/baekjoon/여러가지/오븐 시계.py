
# 0~23 0~59
# 24시간이 되면 다시 0:0시가된다

h,m=map(int,input().split())
plus=int(input())

h_plus=(m+plus)//60
m_na=(m+plus)%60


c=h+h_plus

if c>=24:
    c=c%24
    print(c,m_na)
else:
    print(c,m_na)

    