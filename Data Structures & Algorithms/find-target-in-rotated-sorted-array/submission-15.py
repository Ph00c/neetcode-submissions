"""
two sides left and right 

left - this is the case where the increasing numbers are on the left side 
    - target > mid - can't be on the left of mid
    - target < left pointer - on the search space on the right of variables

right - this is the case where the right half contains the increasing numbers 

    - if the mid is greater than the right pointer 
        close the right side 
    - if the target is less than mid then close the right pointer


"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        
        while l <= r:

            mid = l +(r-l) // 2

            
            if nums[mid] == target:
                return mid

            
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l  = mid+1
                else:
                    r = mid -1 

                
            else:
                if target < nums[mid] or target > nums[r] :
                    r = mid -1 
                else:
                    l = mid+1 


                    

            
            
        return -1
