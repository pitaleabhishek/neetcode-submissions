class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r) // 2
            if nums[m] > target:
                r -= 1
            elif nums[m] < target:
                l += 1
            else:
                return m
        if nums[r] < target:
            return r+1
        elif nums[l] < target and nums[r] > target: 
            return l
        elif nums[l] > target:
            return l
