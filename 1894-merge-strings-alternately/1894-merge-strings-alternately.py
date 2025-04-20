class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = len(word1) if len(word1) > len(word2) else len(word2)
        string = ''
        for i in range(0,l):
            if i < len(word1):
                string += word1[i]
            if i < len(word2):
                string += word2[i]
        return string