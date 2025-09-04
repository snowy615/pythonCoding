def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def even(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return False
    return True

n = int(input())

breakout = False
num_1 = 0
for a in range(1, 10):
    if breakout:
        break
    for b in range(4):
        if breakout:
            break
        for c in range(10):
            if breakout:
                break
            for d in range(2):
                if 1 <= d * 10 + c <= 12 and 1 <= 10 * b + a <= 31 and a*10000001+b*1000010+c*100100+d*11000 > n:
                    year = a * 1000 + b * 100 + c * 10 + d
                    month = d * 10 + c
                    day = 10 * b + a
                    is_leap_year = leap_year(year)
                    if month == 2 and is_leap_year and day >= 30:
                        continue
                    if month == 2 and not is_leap_year and day >= 29:
                        continue
                    even_or_not = even(month)
                    if even_or_not and day >= 31:
                        continue
                    num_1 = a*10000001+b*1000010+c*100100+d*11000
                    breakout = True
                    break

breakout = False
num_2 = 0
for a in range(1, 10):
    if breakout:
        break
    for b in range(0, 2):

        if 1 <= b * 10 + a <= 12 and a * 10100101 + b * 1011010 > n:
            breakout = True
            num_2 = a * 10100101 + b * 1011010
            break


print(num_1)
print(num_2)
