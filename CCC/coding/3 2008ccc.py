# A	B C	D E F
# G	H I	J K	L
# M	N O P Q R
# S	T U V W X
# Y	Z   - . e
word = input()
lista = [0, 0]
total = 0
z = [['A', 'B', 'C', 'D', 'E', 'F'], ['G', 'H', 'I', 'J', 'K', 'L'], ['M', 'N', 'O', 'P', 'Q', 'R'], ['S', 'T', 'U', 'V', 'W', 'X'], ['Y', 'Z', ' ', '-', '.', 'enter']]
for num in range(len(word)):
    for i in range(5):
        if word[num] in z[i]:
            x = i
            y = z[x].index(word[num])
            lista.append(x)
            lista.append(y)
lista.append(4)
lista.append(5)
# print(lista)
for car in range(0, int(len(lista))-2, 2):
    total += abs(lista[car]-lista[car+2]) + abs(lista[car+1]-lista[car+3])
    # print(car)
# print('ha')
print(total)


# .-.-
# 13
# I AM LOST
# 37
# A-B-C
# 31