class Solution:
    def isBoomerang(self, points: [[int]]) -> bool:

        if not points:
            return 

        distance_12 = self.distance(points[0], points[1])
        distance_13 = self.distance(points[0], points[2])

        if distance_12 == distance_13:
            return True
        else:
            return False



    def distance(self, point1: int, point2: int):

        return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

points = [[1,1],[2,3],[3,2]]

# points = [[1,1],[2,2],[3,3]]

ob = Solution()
ans = ob.isBoomerang(points)

ans