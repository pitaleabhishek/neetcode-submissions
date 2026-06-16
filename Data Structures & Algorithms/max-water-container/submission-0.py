class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = (height[l] - height[r]) * min(l, r)


        l, r = 0, len(heights)-1
        res = 0
        while l <= r:
            area = abs((l - r)) * min(heights[l], heights[r])
            res = max(res, area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res


