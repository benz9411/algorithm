


move = input()
row=int(move[1])
column=int(ord(move[0]))-int(ord('a'))+1 
# 이렇게 바꾸면 row 와 column값이 a1 이 들어오면 1,1로 바뀐다.

steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]


result=0
for step in steps:
     next_row = row + step[0]
     next_column = column + step[1]
     if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <= 8:
         result+=1
         
print(result)