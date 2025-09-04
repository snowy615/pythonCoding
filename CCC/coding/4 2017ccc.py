def arithmetic(time):
    r = time[1]-time[0]
    for i in range(len(time)-1):
        if time[i+1]-time[i] != r:
            return False
    return True
hour = ["12", "1", '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
min = []
count = 0
for i in range(10, 60):
    min.append(str(i))
m = int(input())
# hd = m // 720
# m %= 720
h = m // 60
m %= 60
for i in range(h):
    for j in range(50):
        time = list(map(int, hour[i]+min[j]))
        if arithmetic(time) == True:
            # print(f"time = {time}")
            count += 1
if h == 0:
    h = 12
for i in range(m):
    time = list(map(int, str(h) + min[i]))
    if arithmetic(time) == True:
        # print(f"time = {time}")
        count += 1
print(count)
