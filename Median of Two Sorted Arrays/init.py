class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        data_buffer = []
        for element in nums1:
            data_buffer.append( element )
        for element in nums2:
            data_buffer.append( element )

        data_buffer.sort()
        if len( data_buffer ) % 2: res = float( data_buffer[ int( len( data_buffer ) / 2 ) ] )
        else:
            sum_buffer = data_buffer[ int( len( data_buffer ) / 2 - 1 ) ]  + data_buffer[ int( len( data_buffer ) / 2 ) ]
            res = sum_buffer / 2.0
            

        return res
