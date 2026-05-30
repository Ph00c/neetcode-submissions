"""
anagram - strings that contain the same letters

have a way to count all letters in a string

this is the key and store all words with the same letters as the values

return the values
"""



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter)- ord('a') ] += 1 
            res[tuple(count)].append(word)
        return list(res.values())