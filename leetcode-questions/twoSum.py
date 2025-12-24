class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetSet=[]
        nLen = len(nums)
        for index in range(nLen):
            for index2 in range(index+1,nLen):
                if (nums[index]+nums[index2]) == target:
                    targetSet = [index, index2]
                    break
        
        return targetSet