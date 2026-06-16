class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # dict1 = {}

        # for i,num in enumerate(numbers):
        #     diff = target - num
        #     if diff in dict1:
        #         return [dict1[diff]+1, i+1]
        #     dict1[num] = i
        # return
        l, r = 0, len(numbers)-1
        while l<=r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1

