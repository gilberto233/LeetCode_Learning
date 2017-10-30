class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, length, currentLength = [], 0, 0

        index = 0
        while index < len(s):
            if s[index] == '(':
                stack.append(s[index])
            elif s[index] == ')':
                if len(stack) and stack[-1] == '(':
                    stack.pop()
                    stack.append( 2 )

                elif len( stack ) and isinstance( stack[-1], int ):
                    subIndex = len( stack ) - 1
                    while subIndex > 0 and isinstance( stack[ subIndex ], int ):
                        subIndex -= 1
                    if len( stack ) and stack[subIndex] == '(':
                        stack.pop( subIndex )
                        stack.append( 2 )
                    else:
                        stack.append( ')' )
                
            index += 1
        for element in stack:
            if isinstance( element, int ):
                currentLength += element
            else:
                length = max( currentLength, length )
                currentLength = 0

        length = max( length, currentLength )
        return length
    
