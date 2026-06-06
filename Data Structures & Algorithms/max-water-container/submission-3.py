class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #storing max 
        l = 0
        r = len(heights) - 1
        maximumArea = 0
        # checks if moving the smallest value since that determines
        # the max area of water has an instance where the area is greater than the prvious

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


            

        