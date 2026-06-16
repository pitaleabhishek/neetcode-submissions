class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k%len(nums)
        while k:
            elem = nums.pop()
            nums.insert(0, elem)
            k-=1
        return nums
        
