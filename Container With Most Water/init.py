class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        startpoint = 0
        endpoint = len( height ) - 1
        
        while startpoint < endpoint:
            result = max( result, ( endpoint - startpoint ) * min( height[ startpoint ], height[ endpoint ] ) )
            
            if height[ startpoint ] < height[ endpoint]:
                startpoint += 1
            else: endpoint -= 1
        
        return result
