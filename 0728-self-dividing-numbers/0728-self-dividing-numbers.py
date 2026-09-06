class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result=[]
        for num in range(left,right+1):
            n=num
            valid=True
            while n>0:
                digit =n %10
                if digit ==0:
                    valid = False
                    break
                if num % digit !=0:
                    valid =False
                    break
                n=n//10
            if valid:
                result.append(num)
        return result
        