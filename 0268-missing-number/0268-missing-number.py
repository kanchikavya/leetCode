class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        ext_sum=n * (n+1)//2
        actual_sum= sum(nums)
        ssum= ext_sum - actual_sum
        return ssum
        
        