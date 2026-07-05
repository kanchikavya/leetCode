class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l=[]
        for num in nums:
            ans=[]
            while num >0:
                digit=num%10
                ans.append(digit)
                num=num//10
            ans.reverse()
            l.extend(ans)
        return l

        