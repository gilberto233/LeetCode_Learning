class Solution:
  def longestValidParentheses(self, s):
      n, longest, stack = len( s ), 0, []
      
      index = 0
      while index < n:
          if s[ index ] is '(':
              stack.append( index )
          else:
              if len( stack ):
                  if s[ stack[-1] ] is '(':
                      stack.pop()
                  else:
                      stack.append( index )
              else:
                  stack.append( index )
          
          index += 1
          
      if not len( stack ):
          longest = n
      else:
          a, b = n, 0
          while len( stack ):
              b = stack[-1]
              stack.pop()
              longest = max( longest, a - b - 1 )
              a = b
          longest = max( longest, a )
      
      return longest
      
