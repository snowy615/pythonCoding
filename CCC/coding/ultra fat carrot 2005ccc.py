day = round(float(input()), 2)
eve = round(float(input()), 2)
wked = round(float(input()), 2)
if day > 250:
    A = (day-100)*0.25+eve*0.15+wked*0.2
    B = (day-250)*0.45+eve*0.35+wked*0.25
elif day > 100:
    A = (day - 100) * 0.25 + eve * 0.15 + wked * 0.2
    B = eve * 0.35 + wked * 0.25
else:
    A = eve * 0.15 + wked * 0.2
    B = eve * 0.35 + wked * 0.25
A = round(A, 2)
B = round(B, 2)
print('Plan A costs %s'%(A))
print('Plan B costs %s'%(B))
if A < B:
    print('Plan A is cheapest.')
elif A > B:
    print('Plan B is cheapest.')
else:
    print('Plan A and B are the same price.')