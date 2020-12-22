# Given a sorted array of distinct integers and a target value
# Return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        try:
            return nums.index(target)
        except ValueError:
            closest = 0
            difference = 10**4
            
            for i in nums:
                try:
                    if target >= 1 and target < nums[nums.index(i) + 1]:
                        return nums.index(i)
                except IndexError:
                    return nums.index(i) + 1
            return 0
    
        #index = 0
        #for i in nums:
            
           # if i == target:
           #     print(i, "found in nums")
           #     print("index is at: ", index)
           # index += 1
            

