class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return_dict = {}

        for str1 in strs:
            print(''.join(sorted(str1)))
            if (''.join(sorted(str1))) not in return_dict.keys():
                return_dict[(''.join(sorted(str1)))] = [str1]
                print(return_dict)
            elif (''.join(sorted(str1))) in return_dict.keys():
                return_dict[(''.join(sorted(str1)))].append(str1)
        return list(return_dict.values())

