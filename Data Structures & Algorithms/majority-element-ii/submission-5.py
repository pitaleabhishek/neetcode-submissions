class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        if len(nums) == 1:
            return nums
        result = []
        i = 1
        j = 0
        count = 1
        while i < len(nums): 
            while i < len(nums) and nums[i] == nums[j]:
                count += 1
                i += 1
                j += 1
            
            else:
                if count > int(len(nums)/3):
                    result.append(nums[j])
                    print(result)
                    count = 1
                    i += 1
                    j += 1
                else:
                    count = 1
                    i += 1
                    j += 1
        if count > int(len(nums)/3):
            result.append(nums[j])

        return result
