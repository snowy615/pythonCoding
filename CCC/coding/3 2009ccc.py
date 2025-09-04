time = int(input())
print('%s in Ottawa'%time)
l = []
time -= 400
for z in range(5):
    time += 100
    if time > 2359:
        time -= 2400
    elif time < 0:
        time = 2400+time
    l.append(time)
time += 30
if time - int(time/100)*100 > 60:
    b = (time - int(time/100)*100)-60
    time = int(time/100+1)*100 + b
l.append(time)
print('%s in Victoria'%l[0])
print('%s in Edmonton'%l[1])
print('%s in Winnipeg'%l[2])
print('%s in Toronto'%l[3])
print('%s in Halifax'%l[4])
print("%s in St. John's"%l[5])
# 145 in Ottawa
# 2245 in Victoria
# 2345 in Edmonton
# 45 in Winnipeg
# 145 in Toronto
# 245 in Halifax
# 315 in St. John's