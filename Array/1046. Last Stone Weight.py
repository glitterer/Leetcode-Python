class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while True:
            stones.sort()
            # print(stones)
            if len(stones) == 0:
                return 0
            elif len(stones) == 1:
                return stones[0]
            else:
                y = stones.pop()
                x = stones.pop()
                # print(f'x: {x} / y: {y}')

            if x != y:
                stones.append(y-x)
                # python은 garbage collection을 해줄 필요가 없다.
                # if x == y:
                #     del x
                #     del y
                # else:
                #     stones.append(y - x)
