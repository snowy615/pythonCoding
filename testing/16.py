p_1 = list(input())
p_2 = list(input())
p_comb = [0, 0, 0, 0, 0]
for i in range(5):
    one = p_1[i*2].isupper()
    two = p_1[i*2+1].isupper()
    three = p_2[i*2].isupper()
    four = p_2[i*2+1].isupper()
    if (one == False and two == False and three==False and four==False):
        print(0)
        continue
    elif ((one == True and two == False and three == True and four==True) or (one == True and two == True and three == True and four==False) or (one == True and two == True and three == True and four==True) or (one == True and two == True and three == False and four==False)):
        print(1)
        p_comb[i] = 1
    else:
        print(2)
        p_comb[i] = 2
n = int(input())
for i in range(n):
    str = list(input())
    cnt = 0
    for j in range(5):
        if p_comb[j] == 2 or p_comb[j] == str[j].isupper():
            cnt += 1
        else:
            print("Not their baby!")
            break
    if cnt == 5:
        print("Possible baby.")


