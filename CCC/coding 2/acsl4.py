def targetsWithMostArrows(size, targets):
    t_location = targets.split()
    x = [0, 1, 1, 1, 0, -1, -1, -1]
    y = [-1, -1, 0, 1, 1, 1, 0, -1]
    max_cnt = 0
    max_i = []
    for num in range(len(t_location)):
        print(t_location)
        print(f"num = {num}")
        cnt = 8
        for i in range(8):
            # temp_x = t_location[num][0]
            # temp_y = t_location[num][1]
            #index
            t_x_i = int(t_location[num][0])
            t_y_i = int(t_location[num][1])
            while True:
                t_x_i += x[i]
                t_y_i += y[i]
                print(f"index = {str(t_x_i) + str(t_y_i)}")
                if (t_x_i <= 0 or t_x_i >= size-1 or t_y_i <= 0 or t_y_i >= size-1):
                    print(f"out at {t_x_i} {t_y_i}")
                    break

                if (str(t_x_i)+str(t_y_i) in targets):
                    print(f"hit target at {t_x_i} {t_y_i}")
                    cnt -= 1
                    break
        print(cnt)
        if cnt > max_cnt:
            print("replaced as new cnt")
            max_cnt = cnt
            max_i.clear()
            max_i.append(t_location[num])
        elif cnt == max_cnt:
            print("added to lis")
            max_i.append(t_location[num])
        print("_____________________")
    max_i.sort()
    ans = ""
    for j in max_i:
        ans += j + " "
    print(ans)
    return ans

targetsWithMostArrows(5, "31 21 13 32 11 12")
