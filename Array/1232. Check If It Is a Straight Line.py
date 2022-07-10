import math
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x_list = []
        y_list = []
        x_dif, y_dif = [], []
        for x, y in coordinates:
            x_list.append(x)
            y_list.append(y)
        a = [] # 기울기
        for i in range(len(x_list)-1):
            if (x_list[i] - x_list[i+1]) != 0:
                a.append((y_list[i] - y_list[i+1]) / (x_list[i] - x_list[i+1]))
            else:
                a.append(math.inf)
        return len(set(a)) == 1
            
        # a = y[i] - y[i+1] / x[i] - x[i+1]
        # len(set(a)) == 1
