# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from locale import atoi
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_buffer = ''
        l2_buffer = ''

        while not ( l1 == None ):
            l1_buffer = str( l1.val ) + l1_buffer
            l1 = l1.next

        while not ( l2 == None ):
            l2_buffer = str( l2.val ) + l2_buffer
            l2 = l2.next

        data1 = atoi( l1_buffer )
        data2 = atoi( l2_buffer )

        result = data1 + data2
        result_str = list( str( result ) )
        for index in range( len( result_str ) ):
            result_str[ index ] = atoi( result_str[ index ] )
        
        output = []
        for element in result_str:
            output.insert( 0, element )
        return output
