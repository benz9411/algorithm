n,m,w,h=map(int,input().split())
x,y=0,0
x_min=max(x-n,n-w)
y_min=max(y-m,m-h)

result=min(abs(x_min),abs(y_min))

print(result)