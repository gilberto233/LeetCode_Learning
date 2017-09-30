class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        int_str = str( x )
        for index in range( int( len( int_str ) / 2 ) ):
            if not int_str[ index ] == int_str[ len( int_str ) - index - 1 ]:
                return False

        return True
