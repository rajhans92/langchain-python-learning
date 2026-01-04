from typing import List

def maxArea(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    maxArea = 0

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        maxArea = max(maxArea, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

        print(" ===> Left:", left, " Right:", right, " Current Max Area:", maxArea)

    return maxArea

result = maxArea([1,2,6,2,5,4,8,3,7])