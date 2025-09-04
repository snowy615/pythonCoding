def is_monkey(word):
    if word == "A":
        print("YES")
        return True
    if word[0] == "B" and word[-1] == "S":
        is_monkey(word[1:-2])
