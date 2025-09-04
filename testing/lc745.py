words = ["apple", "banana"]
prefix = "a"
suffix = "e"
def f(words, prefix, suffix):
    l = len(words) - 1
    for i in range(l, -1, -1):
        w = words[i]
        l_p = len(prefix)
        if (w[:l_p] == prefix):
            w = w[::-1]
            l_s = len(suffix)
            if (w[:l_s] == suffix):
                return i
    return False
print(f(words, prefix, suffix))