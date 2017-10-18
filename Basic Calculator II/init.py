from locale import atoi
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = 0
        prevIndex = 0
        numStack = []
        numBuffer = ''
        s = s.replace( ' ', '' )

        while index < len( s ) and s[ index ] not in '+-*/':
            index += 1
        numBuffer = s[ prevIndex: index ]
        prevIndex = index + 1
        numStack.append( atoi( numBuffer ) )

        while index < len( s ):
            character = s[ index ]
            index += 1
            while index < len( s ) and s[ index ] not in '+-*/':
                index += 1
            numBuffer = s[ prevIndex: index ]
            prevIndex = index + 1

            if character == '+':
                numStack.append( atoi( numBuffer ) )
            elif character == '-':
                numStack.append( atoi( numBuffer ) * -1 )
            elif character == '*':
                leftCalculatorNumber = numStack.pop()
                numStack.append( atoi( numBuffer ) * leftCalculatorNumber )
            elif character == '/':
                leftCalculatorNumber = numStack.pop()
                numStack.append( int( leftCalculatorNumber / atoi( numBuffer ) ) )

        return sum( numStack )
