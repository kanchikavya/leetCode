class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        s_sum=0
        result=[]
        for i in range(len(nums)):
            s_sum +=nums[i]
            result.append(s_sum)
        return result


        