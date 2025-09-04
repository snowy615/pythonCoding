def count_num(front, back, count):
    if back + front < 2:
        return count
    if back == 0 and front >= 2:
        return count + front - 1
    elif front == 0 and back >= 2:
        return count + back - 1
    elif back == 1:
        return count +(front - 1) * 2 + 1
    elif front == 1:
        return count + (back - 1) * 2 - 1
    else:
        return count +(front + 1) * (back + 1) - 3
def count_cow(Glis, Hlis, n):
    count = 0
    front = Glis[0]
    back = Glis[1]-Glis[0]-1
    count += count_num(front, back, count)
    back = Glis[-1] - Glis[-2] - 1
    front = n-Glis[-1]-1
    count += count_num(front, back, count)
    print(count)

    for i in range(1, len(Glis)-1):
        back = (Glis[i+1] - Glis[i] - 1)
        front = (Glis[i]-Glis[i-1]-1)
        count += count_num(front, back, count)
    print(count)

    front = Hlis[0]
    back = Hlis[1] - Hlis[0] - 1
    count += count_num(front, back, count)
    print(count)
    front = n-Hlis[-1]-1
    back = Hlis[-1] - Hlis[-2] - 1
    count += count_num(front, back, count)
    print(front, back, count)

    for i in range(1, len(Hlis)-1):
        back = (Hlis[i + 1] - Hlis[i] - 1)
        front = (Hlis[i] - Hlis[i - 1] - 1)
        count += count_num(front, back, count)
    return count
n = int(input())
str = input()
count = 0
Glis = []
Hlis = []
for i in range(n):
    if str[i] == "G":
        Glis.append(i)
    else:
        Hlis.append(i)
print(count_cow(Glis, Hlis, n))