class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result=[]
        n1=len(nums1)
        n2=len(nums2)
        if(n1 > n2):

            for i in nums1:

                if(i in nums2 and i not in result):

                    result.append(i)
        else:
            for i in nums2:
                if(i in nums1 and  i not in result):
                    result.append(i)
        return result
        
        