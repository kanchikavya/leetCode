class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if(len(password)<8):
            return False
        is_upper=False
        is_lower=False
        is_digit=False
        is_special=False
        special="!@#$%^&*()-+"
        i=0
        for ch in password:
            if(i>0 and ch == password[i-1]):
                return False
           
            if(ch>='a' and ch<='z'):

                is_upper = True
            elif(ch>='A' and ch<='Z'):

                is_lower= True
            elif(ch>='0' and ch<='9'):

                is_digit= True
            elif(ch in special):
                is_special= True

            i+=1
        return is_upper and is_lower and is_digit and is_special

            
      

        