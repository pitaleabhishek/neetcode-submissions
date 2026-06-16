class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hash_s = {} 
        hash_t = {}


        for char in s:
            if char in hash_s.keys():
                hash_s[char] += 1
            else:
                hash_s[char] = 1

        for char in t:
            if char in hash_t.keys():
                hash_t[char] += 1
            else:
                hash_t[char] = 1

        print(hash_s)
        print(hash_t)
        return hash_s == hash_t

        