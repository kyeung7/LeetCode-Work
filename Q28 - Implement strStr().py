# Return the index of the first occurrence of needle in haystack
# Return -1 if needle is not part of haystack.
# Return 0 if exceeds size bounds

# Results: Runtime: 388ms, Memory: 14.6MB
class Solution(object):
    def strStr(self, haystack, needle):

        # Range constaintsm 
        if len(needle) <= 0 or len(needle) >= 5*(10**4):
            return 0
        
        # Iterate through haystack
        for i in range(len(haystack)):
            
            # Using needle size, look at sets of characters in haystack, return index if found
            if haystack[i:i+len(needle)] == needle:
                return i
        
        # Otherwise not found
        return -1
    
    
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
