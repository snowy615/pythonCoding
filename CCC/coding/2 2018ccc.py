a = int(input())
b = input()
c = input()
sum = 0
for z in range(a):
    if b[z] == c[z]:
        if b[z] == 'C':
            sum += 1
print(sum)