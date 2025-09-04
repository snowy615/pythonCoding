p = int(input())
g = int(input())
r = int(input())
o = int(input())
price = int(input())
m = 2147483640
total_comb = 0
for i in range(int(price/p)+1):
    for j in range(int(price/g)+1):
        for k in range(int(price/r)+1):
            for l in range(int(price/o)+1):
                if i*p + j*g + k*r + l*o == price:
                    m = min(m, i+j+k+l)
                    total_comb += 1
                    print(f"# of PINK is {i} # of GREEN is {j} # of RED is {k} # of ORANGE is {l}")
print(f"Total combinations is {total_comb}.")
print(f"Minimum number of tickets to print is {m}.")