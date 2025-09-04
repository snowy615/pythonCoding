def p(str):
    for i in range(len(str)):
        print(str[i], end="")
instruction = list(input())
while True:
    if "+" not in instruction or "-" not in instruction:
        break
    in_tight = instruction.index("+")
    in_loose = instruction.index("-")
    if in_tight < in_loose:
        p(instruction[:in_tight])
        # for i in range(in_tight+1):
        #     instruction.remove(instruction[i])
        instruction = instruction[in_tight+1:]
        index = 0
        number = ""
        while True:
            num = instruction[index]
            if 47<ord(num)<58:
                number += num
                instruction.remove(num)
            else:
                break
        print(" tighten", end=" ")
        print(int(number))
    else:
        p(instruction[:in_loose])
        instruction = instruction[in_loose+1:]
        index = 0
        number = ""
        while True:
            num = instruction[index]
            if 47 < ord(num) < 58:
                number += num
                instruction.remove(num)
            else:
                break
        print(" loosen", end=" ")
        print(int(number))
while True:
    if "+" not in instruction:
        break
    in_tight = instruction.index("+")
    p(instruction[:in_tight])
    instruction = instruction[in_tight+1:]
    index = 0
    number = ""
    while True:
        if len(instruction) == 0:
            break
        num = instruction[index]
        if 47<ord(num)<58:
            number += num
            instruction.remove(num)
        else:
            break
    print(" tighten", end=" ")
    print(int(number))
while True:
    if "-" not in instruction:
        break
    in_loose = instruction.index("-")
    p(instruction[:in_loose])
    instruction = instruction[in_loose+1:]
    index = 0
    number = ""
    while True:
        if len(instruction) == 0:
            break
        num = instruction[index]
        if 47<ord(num)<58:
            number += num
            instruction.remove(num)
        else:
            break
    print(" loosen", end=" ")
    print(int(number))