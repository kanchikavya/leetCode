from math import factorial
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[]
        for i in range(numRows):
            row=[]
            
                
            for k in range(i+1):
                ncr=factorial(i)//(factorial(k) * factorial(i-k))
                row.append(ncr)
            result.append(row)
        return result
        