
"""
so the current number in the loop is the value we're testing for and we're doing two pointers to find the rest
sorting helps avoid duplicates 

we also need to check if the current number is already a duplicate

we need an update on the pointers to avoid duplicates


[-2,-2 ,0, 0,2,2]
"""



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        nums.sort()

        for i, n in enumerate(nums):
            if n == nums[i-1] and i > 0:
                continue
            l = i+1
            r = len(nums)-1
            while l < r:
                total = nums[l] + nums[r] +nums[i]
                if total > 0:
                    r-=1
                elif total < 0:
                    l+=1 
                else:
                    res.append([nums[l], nums[r],nums[i]])
                    l+=1 
                    while nums[l] == nums[l-1] and l < r:
                        l+=1 
                     
        return res








