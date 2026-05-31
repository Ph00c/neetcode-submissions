"""
let's have a random key separate the words

~ this looksl like a pretty good one 
"""


class Solution:

    def encode(self, strs: List[str]) -> str:
        default =""
        for i in strs:
        
            lenword=len(i)
            default += str(lenword) +"~"+  i
        return default
            

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        lengthWord = len(s)

        while i < lengthWord:
            j = i
            while s[j] != "~":
                j +=1 
            length = int(s[i:j])
            res.append(s[j+1: length+1+j])
            i = j+1+length
        return res






