class Solution:
    def isHappy(self, n: int) -> bool:
        s = set() 
        while True:
            num = 0
            while n >= 10:
                num += (n % 10) * (n % 10)
                n = n // 10
            num += (n % 10) * (n % 10)
            n = num
            if n in s:
                return False
            s.add(n)
            if n == 1:
                return True
