class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.result = True
        self.s = s
        self.startpoint = 0
        self.endpoint = 0

        while self.endpoint < len( self.s ) and self.result:
            if self.s[ self.endpoint ] in "([{":
                self.endpoint = self._pushStack( self.endpoint, s[ self.endpoint ] )
            elif self.s[ self.endpoint ] in "])}":
                self.result = False
                break

            self.endpoint += 1

        return self.result

    def _pushStack(self, startpoint, sign):
        endpoint = startpoint + 1
        while endpoint < len( self.s ) and self.result:
            if self.s[ endpoint ] in "([{":
                endpoint = self._pushStack( endpoint, self.s[ endpoint ] )

            elif self.s[ endpoint ] in "}])":
                if ( sign in '{[' and ord( self.s[ endpoint ] ) - ord( sign ) == 2 ) or ( sign == '(' and ord( self.s[ endpoint ] ) - ord( sign ) == 1 ):
                    self.result = True
                    return endpoint
                else:
                    self.result = False

            endpoint += 1

        self.result = False
        return endpoint
        
        """
        Please refer to the solution given by xiaoying10101
        """
