#input money paid in cents: int(input("Money paid in cents: "))
#input money paid in dollars and convert it to cents
#if the input is negative, the computer will ask for a new input
while True:
    try:
        cmoney = float(input("Money paid in dollars: $"))*100
        cmoney = int(cmoney)
        if cmoney < 0:
            raise Exception()
        else:
            break
    except:
        print("No negative numbers allowed, please try again")


coin_num = 0
print("You will have: ", end="")

#100 dollar bills
hundred = cmoney // 10000
if hundred != 0:
    if hundred == 1:
        print(f"{hundred} hundred dollar bill,", end=" ")
    else:
        print(f"{hundred} hundred dollar bills,", end= " ")
    coin_num += hundred
    cmoney -= hundred*10000

#50 dollar bills
fifty = cmoney // 5000
if fifty != 0:
    if fifty == 1:
        print(f"{fifty} fifty dollar bill,", end= " ")
    else:
        print(f"{fifty} fifty dollar bills,", end=" ")
    coin_num += fifty
    cmoney -= fifty*5000

#20 dollar bills
twenty = cmoney // 2000
if twenty != 0:
    if twenty == 1:
        print(f"{twenty} twenty dollar bill,", end=" ")
    else:
        print(f"{twenty} twenty dollar bills,", end= " ")
    coin_num += twenty
    cmoney -= twenty*2000

#10 dollar bills
ten = cmoney // 1000
if ten != 0:
    if ten == 1:
        print(f"{ten} ten dollar bill,", end=" ")
    else:
        print(f"{ten} ten dollar bills,", end= " ")
    coin_num += ten
    cmoney -= ten*1000

#5 dollar bills
five = cmoney // 500
if five != 0:
    if five == 1:
        print(f"{five} five dollar bill,", end=" ")
    else:
        print(f"{five} five dollar bills,", end= " ")
    coin_num += five
    cmoney -= five*500

#tonnie
two = cmoney // 200
if two != 0:
    if two == 1:
        print(f"{two} tonnie,", end=" ")
    else:
        print(f"{two} tonnies,", end= " ")
    coin_num += two
    cmoney -= two*200

#lonnie
one = cmoney // 100
if one != 0:
    if one == 1:
        print(f"{one} lonnie,", end=" ")
    else:
        print(f"{one} lonnies,", end= " ")
    coin_num += one
    cmoney -= one*100

#quarter
quarter = cmoney // 25
if quarter != 0:
    if quarter == 1:
        print(f"{quarter} quarter,", end=" ")
    else:
        print(f"{quarter} quarters,", end= " ")
    coin_num += quarter
    cmoney -= quarter*25

#dime
dime = cmoney // 10
if dime != 0:
    if dime == 1:
        print(f"{dime} dime,", end=" ")
    else:
        print(f"{dime} dimes,", end= " ")
    coin_num += dime
    cmoney -= dime*10

#nickel
nickel = round(cmoney / 5)
if nickel != 0:
    if nickel == 1:
        print(f"{nickel} nickel,", end=" ")
    else:
        print(f"{nickel} nickels,", end= " ")
    coin_num += nickel
    cmoney -= nickel*5

# #no pennies since we do not use it anymore...
# penny = cmoney
# if penny != 0:
#     print(f"{penny} penny", end= " ")
#     coin_num += penny
if coin_num == 0:
    print("no money", end = "")
else:
    pass
print(f"\nTotal number of bills and coins used: {coin_num}")
