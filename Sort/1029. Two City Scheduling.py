class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0]-x[1])
        ans = 0
        for i in range(len(costs)):
            if i < len(costs)//2:
                ans += costs[i][0]
            else:
                ans += costs[i][1]
        return ans
    
    
        # sorted_costs = sorted(costs, key=lambda x: x[1]-x[0])
        # temp_cost = sum([c[0] for c in sorted_costs])
        # return temp_cost + sum([c[1]-c[0] for c in sorted_costs[:len(costs)//2]])
        
