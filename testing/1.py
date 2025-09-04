class Solution(object):
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = ""
        if len(str) == 0:
            return 0
        for i in str:
            if i == "-":
                num += "-"
            elif ord(i) >= 48 and ord(i) <= 57:
                num += i
            else:
                break
        if len(str) == 0:
            return 0
        return int(num)