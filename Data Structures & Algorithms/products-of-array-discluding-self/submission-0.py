class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return_list = []
        for i in range(len(nums)):
            temp_result = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                temp_result *= nums[j]
            return_list.append(temp_result)
                
        return (return_list)