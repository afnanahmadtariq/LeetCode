class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        i = 0
        l = len(s)
        for char in t:
            if i >= l:
                return True
            elif s[i] == char:
                i += 1
                continue
        if i >= l:
            return True
        return False
