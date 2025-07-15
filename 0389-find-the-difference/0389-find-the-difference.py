class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)  
        t = sorted(t)
        r = 0
        for i, c in enumerate(s):
            r = r ^ ord(c)
            r = r ^ ord(t[i])
        r = r ^ ord(t[-1])
        return chr(r)