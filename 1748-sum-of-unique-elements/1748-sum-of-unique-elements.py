class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum1=0
        for i in range(len(nums)):
            if(nums.count(nums[i])==1):
                sum1+=nums[i]
        return sum1
        