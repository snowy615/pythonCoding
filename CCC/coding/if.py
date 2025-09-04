





e = True
while e == True:
    try:
        a = int(input("Enter a number: "))
        e = False
    except ValueError:
        print("Sorry, that was not a integer. Please try again")
        e = True
if a < 10:
    print("Too small")
elif a > 10:
    print("too large")
else:
    print("The number is 10.")
