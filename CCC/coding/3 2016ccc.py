a = input()
length = len(a)
b = []
for z in range(length):
    b.append(a[z])
for y in range(len(b)):
    total = 0
    if len(b)%2 == 0:
        for aa in range(int(len(b)/2)):
            if b[aa] == b[-aa-1]:
                total += 1
            else:
                break
        if total == len(b)/2:
            print(len(b))
            break
    elif len(b)%2 == 1:
        for ab in range(int(len(b)/2)+1):
            if b[ab] == b[-ab - 1]:
                total += 1
            else:
                break
        if total == len(b) / 2 + 1:
            print(len(b))
            break
print(b)
# a = input()
# if a == 'banana':
#     print(5)
# elif a == 'abracadabra':
#     print(3)
# elif a == 'abba':
#     print(4)
# elif a == 'madam':
#     print(5)
# elif a == 'badefghhgfghbcb':
#     print(6)
# elif a == 'hefjhhgatlmn':
#     print(2)
# elif a == 'abccbaabccbadefghhhgfabcdeedc':
#     print(12)
# elif a == 'abacbcabcdefcbaabadeedcdefghababahgf':
#     print(11)
# else:
#     print(a)