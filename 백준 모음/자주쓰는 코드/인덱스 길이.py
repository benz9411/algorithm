
t="3141592"
p="271"	
        #즉 원래길이 - 비교길이 
for i in range(len(t) - len(p) + 1):
        if int(p) >= int(t[i:i+len(p)]):
            print(t)