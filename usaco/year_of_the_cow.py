animal = ["Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"]
n = int(input())
name = ["Bessie"]
num = [0]
a = ["Ox"]
for i in range(n):
    s = input().split()
    # name, pre/next, animal, name
    #[s[0],      s[3],  s[4], s[-1]]
    name_index = name.index(s[-1])
    previous = s[3]
    years_apart = num[name_index]
    if previous == "previous":
        if animal.index(a[name_index]) > animal.index(s[4]):
            # print("a")
            years_apart -= (animal.index(a[name_index]) - animal.index(s[4]))
        else:
            #print("b")
            years_apart -= animal.index(a[name_index]) +12 - animal.index(s[4])
    else:
        if animal.index(a[name_index]) < animal.index(s[4]):
            #print('c')
            years_apart += animal.index(s[4])-animal.index(a[name_index])
        else:
            #print('d', "years_apart {}".format(years_apart))
            years_apart += animal.index(s[4]) + 12 - animal.index(a[name_index])
    name.append(s[0])
    num.append(years_apart)
    a.append(s[4])
    # print(years_apart)
# print("hello")
# print(name)
# print(num)
print(abs(num[name.index("Elsie")]))