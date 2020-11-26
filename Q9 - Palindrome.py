##Given an array 'nums' and value 'val', remove all instances of the value in place
##and return new length of nums.

# Results: Runtime: 16ms, Memory: 13.4MB
class Solution(object):
    def removeElement(self, nums, val):

        # While list contains value, remove value
        while nums.count(val) != 0:
            nums.remove(val)
        
        return len(nums)

        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
