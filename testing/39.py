i = int(input())
x = 0
for j in range(i+1):
    for k in range(j):
        x+=1
        if x < 10:
            print(f"   {x}", end="")
        elif x < 100:
            print(f"  {x}", end="")
        else:
            print(f" {x}", end=" ")
    print()