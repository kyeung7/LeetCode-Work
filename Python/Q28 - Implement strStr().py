

# Results: Runtime: 16ms, Memory: 13.4MB
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        sizeCheck = len(needle)
        print(sizeCheck)
        
        #string of needle
        #empty string thats updated if matches found
        tempStr = ""
        
        for char in haystack:
            if char in needle:
                tempStr += char
                if tempStr==needle:
                    pass # now return index of instance found
