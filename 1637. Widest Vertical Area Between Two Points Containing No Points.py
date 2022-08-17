class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points)
        return max([sorted_points[i+1][0]-sorted_points[i][0] for i in range(len(sorted_points)-1)])
        

# class Solution:
#     def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
#         sorted_points = sorted(points)
#         diffs = [sorted_points[i+1][0]-sorted_points[i][0] for i in range(len(sorted_points)-1)]
#         return max(diffs)
