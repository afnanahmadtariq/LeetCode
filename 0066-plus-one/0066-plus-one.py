class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i, d in enumerate(digits):
            num += d * 10**(len(digits)-i-1)
        num +=1
        arr = []
        while num > 0:
            arr.insert(0, num%10)
            num = num//10
        return arr