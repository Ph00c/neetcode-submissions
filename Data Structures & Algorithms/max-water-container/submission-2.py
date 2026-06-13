"""
max amount = area -> l * w prob need enumerated list again 

heights[i] = length
i = width

want to get highest area -> max amount that gets updated

have to choose smaller container min()


"""


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        l,r = 0,len(heights)-1
        
        while l < r:
            length = r -l
            height = min(heights[l],heights[r])
            area = length * height
            if area > largest:
                largest = max(area,largest)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1 
        return largest

            