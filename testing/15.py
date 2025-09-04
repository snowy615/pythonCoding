
def countVowelStrings(n):
    res = []
    vowel = ["a", "e", "i", "o", "u"]
    def backtrack(num, s):
        if len(s) == n:
            res.append(s)
            return
        for x in range(num, 5):
            s += vowel[x]
            backtrack(x, s)
    backtrack(0, "")
    return len(res)
print(countVowelStrings(1))
print(countVowelStrings(2))