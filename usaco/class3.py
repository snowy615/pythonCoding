thisdict = {"W":{"po": "m", "performance":71}, "P":{"po": "m", "performance":65}, "M":{"po": "m", "performance":38}, "A":{"po": "m", "performance":53}}
def best_worst():
    best_name = ""
    worse_name = ""
    max_num = 0
    min_num = 1000000
    for a, b in thisdict.items():
        for c, d in b.items():
            # print(a, c, d)
            if c == "performance":
                if int(d) > max_num:
                    best_name = a
                    max_num = d
                if int(d) < min_num:
                    worse_name = a
                    min_num = d

    print(best_name)
    print(worse_name)