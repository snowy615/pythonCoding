"""
ID: yansnow2
LANG: PYTHON3
TASK: friday
"""

fin = open("friday.in", "r")
fout = open("friday.out", "w")
N = int(fin.readline())
week = [0, 0, 0, 0, 0, 0, 0]
daynum = 1
for i in range(1900, 1900+N):
    if (i % 4==0 and i%100) or i%400==0:
        f = 29
    else:
        f = 28
    month = [31, f, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for j in range(len(month)):
        daynum += 12
        week[daynum%7] += 1
        daynum += month[j] - 12
fout.write(f'{week[6]} {week[0]} {week[1]} {week[2]} {week[3]} {week[4]} {week[5]}\n')