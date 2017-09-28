class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        buffer = {}
        maxLen = 0
        start = 0

        for index in range( len( s ) ):
            try:
                if buffer[ s[ index ] ] >= start:
                    start = buffer[ s[ index ] ] + 1
            except: pass
            buffer[ s[ index ] ] = index
            maxLen = max( maxLen, index - start + 1 )

        return maxLen

if __name__ == '__main__':
    test_string = input()
    instance = Solution().lengthOfLongestSubstring( test_string )
    print( instance )
