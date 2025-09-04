ppy = 12000
money_received = 0
for i in range(20):
    money_received += ppy
    money_received *= 1.05
for i in range(67):
    money_received *= 1.05
print(f"money_received = {money_received}")
print(f"money paid = {20*ppy}")
print(f"profit = {money_received-20*ppy}")