class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        index = 0
        while index < len(word1) and index < len(word2):
            s += word1[index] + word2[index]
            index += 1
        if len(word1) < len(word2):
            s += word2[index:]
        elif len(word2) < len(word1):
            s += word1[index:]
        return s