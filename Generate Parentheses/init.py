class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.result = self._generate( n )
        return self.result

    def _generate(self, n):
        buffer = []
        if n == 0:
            buffer.append( '' )
        elif n == 1:
            buffer.append( '()' )
        else:
            for index in range( n ):
                sub_index = n - 1 - index

                for element1 in self._generate( index ):
                    for element2 in self._generate( sub_index ):
                        buffer.append( '(' + element1 + ')' + element2 )

        return buffer
    
