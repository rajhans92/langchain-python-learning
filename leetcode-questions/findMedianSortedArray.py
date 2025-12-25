class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        addList = nums1 + nums2
        addList.sort()
        
        if len(addList)%2:
            return addList[len(addList)//2]
        else:
            return (addList[(len(addList)//2) -1] + addList[len(addList)//2])/2
