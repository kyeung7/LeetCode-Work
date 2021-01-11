class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        returnList = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] + nums[j] == target) and (i != j):
                    if i not in returnList:
                        returnList.append(i)
                    if j not in returnList:
                        returnList.append(j)
        
        return returnList
