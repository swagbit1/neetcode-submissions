class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #storing max 
        l = 0
        r = len(heights) - 1
        maximumArea = 0

        while l < r:
            base = r - l
            area = min(heights[l],heights[r]) * base

            if area > maximumArea:
                maximumArea = area

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maximumArea


            

        