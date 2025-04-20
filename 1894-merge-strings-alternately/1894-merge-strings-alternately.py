class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = list(word1)
        index = 1
        for i in word2:
            l.insert(index, i)
            index +=2
        return "".join(l)