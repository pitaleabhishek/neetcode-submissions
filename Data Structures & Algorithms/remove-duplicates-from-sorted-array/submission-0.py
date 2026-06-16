class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            j = i + 1
            while j < (len(nums)) and nums[i] == nums[j]:
                nums.pop(j)
                
        return len(nums)
        
                