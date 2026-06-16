class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         set1 = set()


         hash_set = {}

         for num in nums:
            if num not in set1:
                set1.add(num)
            else:
                return True
         return False