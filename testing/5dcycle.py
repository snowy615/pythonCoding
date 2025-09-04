for a in range(15):
    for b in range(15):
        for c in range(15):
            for d in range(15):
                if a+b+c+d >= 15:
                    continue
                original = [a, b, c, d]
                lis = [a, b, c, d]
                cnt = 0
                while True:
                    new_lis = lis
                    for i in range(4):
                        if lis[i] >= 3:
                            new_lis[i] -= 1
                            for j in range(4):
                                new_lis[j] += 1
                                print(lis)
                                print(new_lis)
                                print("")
                    lis = new_lis
                    cnt += 1
                    if lis == original:
                        print(f"{a} {b} {c} {d} cnt {cnt}")
                        break
                print("out")