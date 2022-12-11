class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if int(num**.5)**2==num:
            return True
        else:
            return False