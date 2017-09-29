class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = 0
        left = 0
        right = 0
        startpoint = 0
        endpoint = 0
        for index in range( 1, len( s ) ):
            # occasion one
            if not ( index == len( s ) - 1 ) and s[ index - 1 ] == s[ index + 1 ]:
                left = index - 1
                right = index + 1

                while ( left - 1 ) >= 0 and ( right + 1 ) <= len( s ) - 1 and s[ left - 1 ] == s[ right + 1 ]:
                    left -= 1
                    right += 1
            if (right - left + 1) > length:
                length = right - left + 1
                startpoint = left
                endpoint = right

            if s[ index - 1 ] == s[ index ]:
                left = index - 1
                right = index

                while ( left - 1 ) >= 0 and ( right + 1 ) <= len( s ) - 1 and s[ left - 1 ] == s[ right + 1 ]:
                    left -= 1
                    right += 1
            if ( right - left + 1 ) > length:
                length = right - left + 1
                startpoint = left
                endpoint = right

        return s[ startpoint: endpoint + 1 ]

if __name__ == '__main__':
    s = input()
    instance = Solution().longestPalindrome( s )
    print( instance )
