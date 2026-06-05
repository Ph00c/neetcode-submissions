class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerS = s.lower()
        l,r = 0,len(lowerS)-1
        while l <= r:
            if self.isAlphaNum(lowerS[l]) == False:
                l += 1
                continue
            if self.isAlphaNum(lowerS[r]) == False:

                r-=1 
                continue
            if lowerS[l] != lowerS[r]:
                return False
            l+=1
            r-=1 
        return True
             




    def isAlphaNum(self,s:str)->bool:

        if ord('A') <= ord(s) <= ord('Z') or ord('a') <= ord(s) <= ord('z') or ord('0') <= ord(s) <= ord('9'):
            return True
        else: 
            return False        