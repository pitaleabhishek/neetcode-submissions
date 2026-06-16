class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return_list = []
        prefix = [] 
        suffix = []
        temp_result = 1
        for i in range(1, len(nums)):
            temp_result *= nums[i-1]
            prefix.append(temp_result)


        temp_result = 1
        for i in (range(len(nums)-2, -1, -1)):
            temp_result *= nums[i+1]
            suffix.append(temp_result)


        prefix.insert(0, 1)
        suffix.insert(0, 1)
        print(prefix)   
        print(suffix)
        for i in range(len(nums)):
            result = prefix[i] * suffix[len(nums)-i-1]
            return_list.append(result)
        return (return_list)