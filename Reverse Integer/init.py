class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = 0
        if x > 0: s = 1
        else: s = -1

        r = int( str( abs( x ) )[ ::-1 ] )
        return s * r * ( r < 2 ** 31 )
        
