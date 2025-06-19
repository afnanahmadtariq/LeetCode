class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        l = list(counter.values())
        s = set(l)
        if len(s) == 1 and l[0] == 1:
            return False
        else:
            return True