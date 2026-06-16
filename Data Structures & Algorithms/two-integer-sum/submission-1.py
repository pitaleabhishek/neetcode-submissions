class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_num = {}

        for i, num in enumerate(nums):
            if (target - num) not in hash_num:
                hash_num[num] = i
            else:
                return [hash_num[target - num], i]
        