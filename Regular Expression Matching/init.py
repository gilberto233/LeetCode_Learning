class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len( s )
        n = len( p )
        dp = {}
        for i in range( m + 1 ):
            dp[ i ] = {}
            for j in range( n + 1 ):
                dp[ i ][ j ] = False

        dp[0][0] = True
        for index in range( m + 1 ):
            for sub_index in range( 1, n + 1 ):
                if p[ sub_index - 1 ] == '*':
                    dp[index][sub_index] = dp[index][sub_index - 2] or (index > 0 and (s[index - 1] == p[sub_index - 2] or p[sub_index - 2] == '.') and dp[index - 1][sub_index])
                else:
                    dp[index][sub_index] = index > 0 and dp[index - 1][sub_index - 1] and (s[index - 1] == p[sub_index - 1] or p[sub_index - 1] == '.')

        return dp[ m ][ n ]
