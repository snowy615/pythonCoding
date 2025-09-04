#bin() int(n, 2)
# print(bin(10).strip("0b")) #101
# print(int("100", 2)) #4
# print(int("1111111111", 2))
count = 0
for i in range(1024):
    bi = bin(i).strip("0b")
    abba = False
    for j in range(len(bi)-3):
        if bi[j] == "1" and bi[j+1] == "0" and bi[j+2] == "0" and bi[j+3] == "1":
            abba = True
            break
    if abba == False:
        count += 1
print(count)