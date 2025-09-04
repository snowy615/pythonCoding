def is_num(x):
    num_1 = list(str(x))
    num_2 = list(str(x))
    num_2.reverse()
    for j in range(len(num_2)):
        if num_2[j] == '6':
            num_2[j] = '9'
        elif num_2[j] == '9':
            num_2[j] = '6'
        elif num_2[j] == '0' or num_2[j] == '1' or num_2[j] == '8':
            pass
        else:
            return False
    if num_1 == num_2:
        return True
    else:
        return False

m = int(input())
n = int(input())
count = 0
for i in range(m, n):
    if is_num(i) == True: count += 1
print(count)