p1, p2, p3 = map(int, input().split())
t1, t2, t3 = map(int, input().split())
t_total = t1+t2+t3
price = p1*t1+p2*t2+p3*t3
print(t_total, price)