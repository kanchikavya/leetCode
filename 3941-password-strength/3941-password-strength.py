class Solution:
    def passwordStrength(self, password: str) -> int:
        uniq=set(password)
        total=0
        for ch in uniq:
            if(ch>='a' and ch<='z'):
                total+=1
            elif(ch>='A' and ch<='Z'):
                total+=2
            elif(ch>='0' and ch<='9'):
                total+=3
            else:
                total+=5
        return total
        
        