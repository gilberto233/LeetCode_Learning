from locale import atoi
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        self.index = 0
        #self.stack = []

        return self._calculateStack()


    def _calculateStack(self):
        result = 0
        subIndex = self.index
        operator = '+'
        while self.index < len(self.s):
            subIndex = self.index
            if self.s[self.index] in "+-() ":
                if self.s[ self.index ] == '+':
                    operator = '+'
                elif self.s[ self.index ] == '-':
                    operator = '-'
                elif self.s[ self.index ] == '(':
                    self.index += 1
                    if operator == '+':
                        result += self._calculateStack()
                    elif operator == '-':
                        result -= self._calculateStack()
                elif self.s[ self.index ] == ')':
                    return result
                elif self.s[ self.index ] == ' ':
                    self.index += 1
                    continue
            else:
                while subIndex < len( self.s ) and self.s[ subIndex ] not in "()+- ":
                    subIndex += 1
                if operator == '+':
                    result += atoi(self.s[self.index: subIndex])
                elif operator == '-':
                    result -= atoi(self.s[self.index: subIndex])
                self.index = subIndex - 1

            self.index += 1

        return result
        
