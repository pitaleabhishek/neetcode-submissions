class Solution:
    def trap(self, height: List[int]) -> int:
        max_left_h = [0] * len(height)
        max_right_h = [0] * len(height)

        max_h = height[0]
        for i in range(1, len(height)):
            max_left_h[i] = max_h
            max_h = max(max_h, height[i])

        max_h = height[-1]
        for i in reversed(range(1, len(height))):
            max_right_h[i] = max_h
            max_h = max(max_h, height[i])


        max_area = 0
        for i in range(len(max_left_h)):
            area = 0
            if min(max_left_h[i], max_right_h[i]) - height[i] > 0:
                area = min(max_left_h[i], max_right_h[i]) - height[i]
                max_area += area
        return max_area