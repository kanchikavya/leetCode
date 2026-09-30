class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n=len(nums)
        # rotations = k % n
        # for _ in range(rotations):
        #     # if()
        #     last_ele=nums.pop()
        #     nums.insert(0,last_ele)
        # return nums
        n=len(nums)
        k=k % n
        nums[:] = nums[-k:] + nums[:-k]
       



        