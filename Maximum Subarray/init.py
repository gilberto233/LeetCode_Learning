class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        dp = []
        dp.append( nums[0] )
        maxSum = nums[0]

        for index in range( 1, len( nums ) ):
            if dp[ index - 1 ] > 0:
                dp.append( nums[ index ] + dp[ index - 1 ] )
            else:
                dp.append( nums[ index ] )

            maxSum = max( maxSum, dp[ index ] )

        return maxSum
        
