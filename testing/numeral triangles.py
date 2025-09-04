start, delta, row = map(str, input().split())
start=int(start,8)
delta=int(delta,8)
row=int(row)
start_num = int(row*(row-1)/2)
end_num = int((row*(row+1)/2))
s_number =start + start_num*delta
e_number =start + end_num*delta
count = 0
for i in range(s_number, e_number, delta):
    s = oct(i)
    for j in range(2,len(s)):
        count += int(s[j])
print(count)
