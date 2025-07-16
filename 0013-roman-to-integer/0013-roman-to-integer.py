class Solution:
    def romanToInt(self, s: str) -> int:
        hash = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        num = 0
        flag = False
        for i, char in enumerate(s):
            if flag:
                flag = False
                continue
            if i+1 < len(s):
                if (char == 'I' and (s[i+1] == 'V' or s[i+1] == 'X')) or(char == 'X' and (s[i+1] == 'L' or s[i+1] == 'C')) or (char == 'C' and (s[i+1] == 'D' or s[i+1] == 'M')):
                    num += hash[s[i+1]] - hash[char]
                    flag = True
                else:
                    num += hash[char]
            else:
                num += hash[char]
        return num