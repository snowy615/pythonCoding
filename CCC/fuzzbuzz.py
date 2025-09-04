for i in range(1, 150):
    t=True
    if i%3==0:
        t=False
        print("fizz", end=" ")
    if i%5==0:
        t=False
        print("buzz", end=" ")
    if t:
        print(f"{i} ", end="")