class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        
        for index in range( len( nums ) ):
            remain = target - nums[ index ]
            
            for sub_index in range( index + 1, len( nums ) ):
                if remain == nums[ sub_index ]:
                    result.append( index )
                    result.append( sub_index )
                    return result
                    
