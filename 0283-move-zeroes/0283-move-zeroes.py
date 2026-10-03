class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
     
        # i = 0

        # for j in range(len(nums)):
        #     if nums[j] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1
        # l=[]
        j=0

        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[i],nums[j]=nums[j],nums[i]
                # l.append(nums[i])
        # for i in range(len(nums)):
        #     if(nums[i]==0):
                j+=1

                # l.append(nums[i])
                # return l
        # return nums[j]