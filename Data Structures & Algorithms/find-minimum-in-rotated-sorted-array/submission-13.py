"""
list nums gets rotated

there's a larger half and a smaller half 
[3,4,5,6,1,2]
 |      ||  |
 larger   smaller

 [6,1,2]


"""




class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0 ,len(nums) -1
        smallest = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                smallest = min(smallest,nums[l])
                break


            mid = l+ (r-l) // 2 
            smallest = min(smallest,nums[mid])
            if nums[mid] >= nums[l]:
                l = mid+1
            else:
                r = mid- 1 
        
        return smallest


