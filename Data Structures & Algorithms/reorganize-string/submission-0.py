class Solution:
    def reorganizeString(self, s: str) -> str:
        
        res = []
        res2 = []
        dict1 = {}
        for elem in s:
            if elem in dict1:
                dict1[elem] += 1
            else:
                dict1[elem] = 1
        i = 0
        for k, v in dict1.items():
            res.append([k,v, i])
            i += 1            
        while len(res) > 0:
            added = False
            res.sort(key=lambda x: -x[1])
            for elem in res[:]:
                if len(res2) != 0 and res2[-1] == elem[0]:
                    continue
                else:
                    res2.append(elem[0])
                    elem[1] -= 1
                    if elem[1] == 0:
                        res.remove(elem)
                    added = True
                    break
                
            if not added:   # FIX → no valid char found
                print("")   # not possible
                break

        return ("".join(res2) if len(res) == 0 else "")

        
            
        