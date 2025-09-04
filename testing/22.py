money = int(input())
m_1 = int(input()) #35 -> 30
m_2 = int(input()) #100 -> 60
m_3 = int(input()) #10 -> 9
count = 0
while money > 0:
    m_1 += 1
    if m_1 == 35:
        money += 30
        m_1 = 0
    count += 1
    money -= 1
    if money == 0:
        break
    m_2 += 1
    if m_2 == 100:
        money += 60
        m_2 = 0
    count += 1
    money -= 1
    if money == 0:
        break
    m_3 += 1
    if m_3 == 10:
        money += 9
        m_3 = 0
    count += 1
    money -= 1
print(f"Martha plays {count} times before going broke.")