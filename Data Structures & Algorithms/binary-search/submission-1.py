class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()

        l, r = 0, len(nums)-1

        while l<=r:
            m = (l+r) // 2

            if target > nums[m]:
                l += 1
            elif target < nums[m]:
                r -= 1

            else:
                return m   
        return -1    