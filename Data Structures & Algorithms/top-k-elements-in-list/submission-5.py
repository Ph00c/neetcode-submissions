"""
heaps store the max and min amount of values in a tree format

push to the heap and if it exceeds a certain length then pop 

need a way to count the frequencies of numbers 

"""
import heapq 
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        #freq, freq.values(), freq.items()
        for num,freqs in freq.items():
            heapq.heappush(heap,(freqs,num)) # remember to return the variable not the list 
            if len(heap) > k:
                heapq.heappop(heap)
                
        res = []
        
        for _,i in heap:
            res.append(i)
        return res
            

            
        
        
        