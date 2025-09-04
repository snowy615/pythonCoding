"""
ID: yansnow2
LANG: PYTHON3
TASK: gift1
"""


fin = open("gift1.in", "r")
fout = open("gift1.out", "w")
NP = int(fin.readline())
dict = {fin.readline():0 for i in range(NP)}

for j in range(NP):
    name = fin.readline()
    lis = list(map(int, fin.readline().split()))
    ppp = 0
    if lis[1] != 0:
        ppp = int(lis[0]/lis[1])
    dict[name] -= ppp*lis[1]
    for z in range(lis[1]):
        name = fin.readline()
        dict[name] += ppp


for name,value in dict.items():
    name=name.replace('\n',' ')
    fout.write(f'{name}{value}\n')
fin.close()
fout.close()