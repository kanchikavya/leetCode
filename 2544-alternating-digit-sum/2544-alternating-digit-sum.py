class Solution:
    def alternateDigitSum(self, n: int) -> int:
        count=len(str(n))
        rev=0
        l=[]
        for i in range(count):
            digit=n%10
            l.append(digit)
            t=rev*10+digit
            n=n//10
        l.reverse()
        ans=0
        for i in range(len(l)):
            if(i % 2==0):
                ans +=l[i]
            else:
                ans -=l[i]
        return ans
        