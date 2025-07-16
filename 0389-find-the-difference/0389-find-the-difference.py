class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(t) - Counter(s)
        return count.most_common(1)[0][0]