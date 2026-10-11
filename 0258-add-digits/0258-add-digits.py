class Solution:
    def addDigits(self, num: int) -> int:

        # return (1+ (num -1) % 9)
        while(num > 9):
            d_sum=0
            while(num > 0):
                d_sum+=num % 10
                num= num //10
            num= d_sum
        return num
        