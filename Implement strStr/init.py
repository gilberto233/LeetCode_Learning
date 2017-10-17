class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = 0
        matchLength = len( needle )
        if not matchLength:
            return 0

        while index < len( haystack ) - matchLength + 1:
            if haystack[ index ] == needle[0]:
                if haystack[ index: index + matchLength ] == needle:
                    return index

            index += 1

        return -1
    
