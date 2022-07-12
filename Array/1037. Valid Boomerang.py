import math
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        ans = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                if (points[i][0]-points[j][0]) == 0:
                    ans.append(math.inf) # [[0,0],[1,0],[2,2]]
                else:
                    ans.append((points[i][1]-points[j][1]) / (points[i][0]-points[j][0]))
            # [[0,1],[1,0],[0,1]]
            # constraints points.length == 3라서 가능하다
            if len(set(ans)) == 3:
                return True
        return False
    
    
    '''
    # discussion의 다른 사람의 답을 보니 "삼각형의 넓이 != 0"이라는 특징을 사용해서도 풀수 있네요
		x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        
        area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2
        return area != 0
    '''
