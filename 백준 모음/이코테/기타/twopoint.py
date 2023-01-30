n=5
m=5
data=[1,2,3,2,5]
data.sort()
count = 0

end=0
interval_sum=0
for start in range(n):
    #start 지점을 처음으로 나두고 end를 움직이는 반복문
    while interval_sum<m and end<n: #부분합이 m 보다 작고 end가 n보다 작고
        print(f"start는{start} inter은{interval_sum}")
        interval_sum+=data[end]
        end+=1
    #여기서 end가 움직이는 기준은 부분합이 원하는 값보다 작은 경우 커지게 하기 위해서 뒤로
    if interval_sum ==m:
        count+=1
    interval_sum-=data[start]
    
print(count)