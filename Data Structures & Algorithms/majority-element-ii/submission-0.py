class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        



        dict1 = {}
        result = []
        for num in nums:
            if num not in dict1:
                dict1[num] = 1
            else:
                dict1[num] += 1

        for k, v in dict1.items():
            if v > int(len(nums)/3):
                result.append(k)

        return result