a=int(input())
for i in range(a):
    ns = int(input())
    nv = int(input())
    no = int(input())
    s = []
    v = []
    o = []
    for x in range(ns):
        s.append(input())
    for y in range(nv):
        v.append(input())
    for z in range(no):
        o.append(input())
    for x in range(ns):
        for y in range(nv):
              for z in range(no):
                  print("%s %s %s."%(s[x],v[y],o[z]))
    print()
