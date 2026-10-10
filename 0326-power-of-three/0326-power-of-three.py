class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # temp = n
        if(n<=0):
            return False
        else:
            temp = n
         
            while(temp % 3==0 ):
                temp = temp //3
                # return True 
            if(temp == 1):
                
                return True
            return False
            
        