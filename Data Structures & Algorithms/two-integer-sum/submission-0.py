class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        hash_set = {}

        for i, num in enumerate(nums):
            
            if (target - num) in hash_set.keys():
                return [hash_set[target-num], i]
            hash_set[num] = i


