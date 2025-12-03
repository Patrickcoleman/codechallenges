points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]

class Solution:
    def countTrapezoids(self, points) -> int:
        slopes = {}

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                p1 = points[i]
                p2 = points[j]
                p1x = points[i][0]
                p2x = points[j][0]
                p1y = points[i][1]
                p2y = points[j][1]
                slope = (p2y-p1y)/(p2x-p1x)
                print(f"Slope between point {points[i]} and {points[j]}: {slope}")


        return -100

print(Solution.countTrapezoids(Solution, points))

        