class Solution:
    def isPalindrome(self,s: str) -> bool:
        lowerS = s.lower()
        l,r = 0,len(lowerS)-1

        while l <= r:
            if lowerS[l].isalnum() == False:
                l += 1
                continue
            if lowerS[r].isalnum() == False:
                r-=1 
                continue
            if lowerS[l] != lowerS[r]:
                return False
            l+=1
            r-=1 
        return True