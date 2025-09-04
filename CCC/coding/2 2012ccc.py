a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < b and b < c and c < d:
    print('Fish Rising')
elif a > b and b > c and c > d:
    print('Fish Diving')
elif a == b and b == c and c == d:
    print('Fish At Constant Depth')
else:
    print('No Fish')