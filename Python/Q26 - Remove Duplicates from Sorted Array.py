## Given sorted array 'nums', remove duplicates in place so each element appears
## only once and returns the new length of the array. Do not allocate space for
## another array. You must modify the input array.

# Results: Runtime: 2560ms, Memory: 15.2MB
class Solution(object):
    def removeDuplicates(self, nums):
        
        # Iterate through nums list
        for item in nums:
            # print("checking: ", item) # For debugging
            
            # While there are more then 1 of item in list
            while nums.count(item) > 1:
                
                # Remove item duplicate from list
                nums.remove(item)
                # print("removing ", item, "new list: ", nums)  # For debugging
        
        # Return new length of nums
        return len(nums)
    
    
        """
        :type nums: List[int]
        :rtype: int
        """

## THIS ONE DOES NOT MEET REQ
##        newNums = [] #make new empty list
##        
##        for item in nums: #iterate through list
##           # print(item) for debugging
##            
##            if item not in newNums: #check if num already in temp list
##                newNums.append(item) #if not add it
##            else: #otherwise remove from current list
##                nums.pop(item)
##        
