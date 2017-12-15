class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return self._recursion( n )

    def _recursion(self, level):
        if level is 1:
            return '1'
        else:
            buffer = self._recursion( level - 1 )
            result = ''
            counter = []

            prevChar = buffer[0]
            for index in range( len( buffer ) ):
                if buffer[ index ] != prevChar:
                    result += ( str( len( counter ) ) + prevChar )
                    prevChar = buffer[ index ]
                    counter.clear()
                    #counter.append( buffer[ index ] )
                #else:
                    #counter.append( buffer[ index ] )
                counter.append( buffer[ index ] )
            #if buffer:
            #    result += ( str( len( counter ) ) + prevChar )
            result += ( str( len( counter ) ) + prevChar )

            return result
