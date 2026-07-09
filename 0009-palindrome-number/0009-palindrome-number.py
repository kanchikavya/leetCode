class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if(x<0):
            return False
        #     sign=-1
        #     x=-x
        # else:
        #     sign=1
        rev=0
        temp=x
        while(x>0):
            digit=x%10
            rev=rev*10+digit
            x=x//10
        if(rev==temp):
            return True
        else:
            return False
    
    
        

        