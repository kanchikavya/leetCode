class Solution:
    def alternateDigitSum(self, n: int) -> int:
        # count=len(str(n))
        l=[]
        rev=0
        while(n>0):
            digit=n%10
            l.append(digit)
            n=n//10
        l.reverse()
        result=0
        for i in range(len(l)):
            if(i % 2==0):
                result +=l[i]
            else:
                result -=l[i]
        return result

