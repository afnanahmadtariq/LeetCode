class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        if len(s) != len(t):
            return False
        table = {}
        i = 1
        for i, char in enumerate(s):
            if char not in list(table.keys()):
                table[char] = i
            s[i] = table[char]
        table = {}
        i = 1
        for i, char in enumerate(t):
            if char not in list(table.keys()):
                table[char] = i
            t[i] = table[char]
        return s == t
