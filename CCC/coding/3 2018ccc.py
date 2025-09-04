num = input()
num = num.split(' ')
total = 0
numa = []
for y in range(len(num)):
    numa.append(int(num[y]))
# print(numa)
ab = numa[0]
bc = numa[1]
cd = numa[2]
de = numa[3]
print('%s %s %s %s %s' %(0, ab, ab+bc, ab+bc+cd, ab+bc+cd+de))
print('%s %s %s %s %s' %(ab, 0, bc, bc+cd, bc+cd+de))
print('%s %s %s %s %s' %(ab+bc, bc, 0, cd, cd+de))
print('%s %s %s %s %s' %(ab+bc+cd, bc+cd, cd, 0, de))
print('%s %s %s %s %s' %(ab+bc+cd+de, bc+cd+de, cd+de, de, 0))
# print(l)