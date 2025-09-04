def findNumber(arr, k):
    # Write your code here
    try:
        ix = arr.index(k)
        return "YES"
    except:
        return "NO"

def oddNumbers(l, r):
    ar = []
    if l % 2==0:
        for i in range(l+1, r+1, 2):
            ar.append(i)
    else:
        for i in range(l, r+1, 2):
            ar.append(i)
    return ar