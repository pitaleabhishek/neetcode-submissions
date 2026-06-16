class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for item in strs:
            length = len(item)

            result += str(length) + "#" + item

        return result


        # result = "0#2#Vn"

    def decode(self, s: str) -> List[str]:
        result2 = []
        
        i = 0
        while i < len(s): 
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start_index = j + 1
            stop_index = start_index + length
            string_formed = s[start_index:stop_index]
            result2.append(string_formed)
            i = stop_index

        return result2



