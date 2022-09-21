class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        remain = capacity
        steps = 0
        for i in range(len(plants)):
            if remain >= plants[i]:
                steps += 1 # 다음 plant
            else:
                steps += 2*i + 1
                remain = capacity # refill
            remain -= plants[i]
        return steps

'''
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        remain = capacity
        steps = 0
        for i in range(len(plants)):
            if remain >= plants[i]:
                remain = remain - plants[i]
                steps += 1 # 다음 plant
            else:
                steps += i # river로 돌아가기
                steps += i+1 # plant로 돌아감
                remain = capacity # refill
                remain = remain - plants[i]
        return steps
'''
