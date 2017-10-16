class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        tag = 0

        for index in range( len( nums ) ):
            if not nums[ index ] == val:
                nums[ tag ] = nums[ index ]
                tag += 1

        return tag
        
