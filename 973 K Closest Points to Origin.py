class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda point: math.pow(math.pow(point[0], 2) + 
            math.pow(point[1], 2), 0.5))
        return points[:k]
