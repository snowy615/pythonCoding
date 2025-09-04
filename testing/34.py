#2 -3
# def f(x):
#     if x%2==1 and x>0: return 3+f(x-3)
#     elif x%2==0 and x>0: return 2-f(x+1)
#     else: return 5
# print(f(5))


def f(x):
    if x>1: return f(f(x-2))+1
    elif x==1: return 2
    else: return 1
print(f(6))