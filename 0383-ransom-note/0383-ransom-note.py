class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = list(ransomNote)
        m = list(magazine)
        for char in r:
            if char in m:
                m.remove(char)
            else:
                return False
        return True