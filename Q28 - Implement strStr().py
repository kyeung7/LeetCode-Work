

# Results: Runtime: 16ms, Memory: 13.4MB
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        print("needle: ", needle, " size: ", len(needle))
        if len(needle) == 0:
            return 0
        
        i = 0
        while i < len(haystack):
            
            if haystack[i:i+len(needle)] == needle:
                print("match found at index: ", i)
                return i
                
            print(haystack[i: i+len(needle)])
            
            i+=1
        
        return -1
