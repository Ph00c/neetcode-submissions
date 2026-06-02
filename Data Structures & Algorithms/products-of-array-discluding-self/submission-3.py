"""
we want a single pass solution 

prefix and suffix implementation 

multiply one way from left to right by prefix
multiply from right to left by suffix 



"""



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]
        
        suffix= 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
