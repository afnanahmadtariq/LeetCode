class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = list(t)
        i = 0
        l = len(s)
        for char in t:
            if i >= l:
                return True
            elif s[i] == char:
                i += 1
                continue
        return i == l
