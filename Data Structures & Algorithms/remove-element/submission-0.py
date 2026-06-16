class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        while val in nums:
            nums.remove(val)
            count += 1

        res = len(nums)

        return res
        