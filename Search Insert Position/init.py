class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        if not len( nums ):
            return 0

        while index < len( nums ):
            if not nums[ index ] < target:
                return index

            index += 1

        return len( nums )
    
