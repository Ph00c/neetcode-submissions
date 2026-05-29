
"""
array of strings 

anagram - words that contains the same letters, can have diff order 

traverse string and use freq table to count the letters - start at 0 if value not assigned

strs = ["act","pots","tops","cat","stop","hat"] - act - a += 1 c += 1 t +=1 

caveate - using ascii value but they need to start at 0 


using the count as keys to the hashmap - this fetches the word to return as a list



- lists can't be keys becuase they are mutable 
    - turn them into tuples which are immutatble 


you can manipulate keys as easily as values 





"""




class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for letter in string:
                count[ord(letter) - ord('a')] += 1
            
            res[tuple(count)].append(string)

        return list(res.values())
    




