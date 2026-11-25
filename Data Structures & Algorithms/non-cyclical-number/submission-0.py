class Solution:
    def isHappy(self, n: int) -> bool:
        h = set()
        while n != 1:
            total = 0
            while n != 0:
                digit = n%10
                total += digit**2
                n = n//10
            if total in h:
                return False
            h.add(total)
            n = total
        return True