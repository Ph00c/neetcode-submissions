
"""
We know a sequence starts when the number right before it doesn't exist in the list 
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        longest = 0
        currLen = 0
        for num in nums:
            if num-1 not in arr:
                curr =num
                currLen = 1
                while curr+1 in arr:
                    curr = curr+1
                    currLen+=1
            longest = max(longest,currLen)
        return longest 
            

