n=input()


front=list(n[:len(n)//2])

back=list(n[(len(n)//2):])

front_new=sum(list(map(int,front)))
back_new=sum(list(map(int,back)))


if front_new==back_new:
    print('LUCKY')
else:
    print('READY')
