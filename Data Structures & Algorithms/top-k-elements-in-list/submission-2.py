class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for n in nums:
            if n not in dict1:
                dict1[n] = 1
            else:
                dict1[n] += 1
        sorted_dict1 = dict(sorted(dict1.items(), key = lambda item: item[1],reverse=True))
        print(sorted_dict1)
        res = []

        

        for key, val in sorted_dict1.items():
            res.append(key)
            k -= 1
            if k == 0:
                return res






