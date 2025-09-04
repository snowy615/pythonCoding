number_of_times = int(input())
input_number_1= int(input())
input_number_2 = int(input())
input_number_3 = int(input())
a = []
b = []
c = []
for z in range(input_number_1):
    a.append(input())
for y in range(input_number_2):
    b.append(input())
for x in range(input_number_3):
    c.append(input())

for w in range(len(a)):
    for v in range(len(b)):
        for u in range(len(c)):
            print(a[w],b[v],c[u])