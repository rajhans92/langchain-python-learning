class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        totalApple = sum(apple)
        capacity.sort()
        minBox = 0

        for box in capacity[::-1]:
            totalApple = totalApple - box
            minBox+=1
            if totalApple <=0:
                break

        return minBox