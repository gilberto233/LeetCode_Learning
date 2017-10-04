class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        
        for index in range( nums.__len__() - 2 ):
            startpoint, endpoint = index + 1, nums.__len__() - 1
            if index > 0 and ( nums[ index ] == nums[ index - 1 ] ):
                continue
            
            while startpoint < endpoint:
                num_sum = nums[ index ] + nums[ startpoint ] + nums[ endpoint ]
                
                if num_sum > 0:
                    endpoint -= 1
                elif num_sum < 0:
                    startpoint += 1
                else:
                    result.append( [ nums[ index ], nums[ startpoint ], nums[ endpoint ] ] )
                    while ( startpoint < endpoint ) and ( nums[ startpoint ] == nums[ startpoint + 1 ] ):
                        startpoint += 1
                    while ( startpoint < endpoint ) and ( nums[ endpoint ] == nums[ endpoint - 1 ] ):
                        endpoint -= 1
                    startpoint += 1
                    endpoint -= 1
                    
        return result
                        
