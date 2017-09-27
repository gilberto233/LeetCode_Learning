from locale import atoi
class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        result = 0

        cover = 0
        for index in range( len( ops ) ):
            index -= cover

            if ops[ index ] == 'C':
                ops.pop( index )
                ops.pop( index - 1 )
                cover += 2
            elif ops[ index ] == 'D':
                ops[ index ] = ops[ index - 1 ] * 2
            elif ops[ index ] == '+':
                ops[ index ] = ops[ index - 1 ] + ops[ index - 2 ]
            else: ops[ index ] = atoi( ops[ index ] )

        result = sum( ops )
        return result

if __name__ == '__main__':
    test_data = input().strip( '[]"' ).split( '","' )
    instance = Solution().calPoints( test_data )
    print( instance )
