class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            a, b = stones.pop(), stones.pop()
            print("a: ", a, "b: ", b)
            if a == b:
                continue
            else:
                result = abs(a - b)
                stones.append(result)
        return stones[0] if len(stones) == 1 else 0