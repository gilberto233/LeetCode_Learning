# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sortList = []

        while True:
            if not l1:
                while l2:
                    sortList.append( l2.val )
                    l2 = l2.next
                break
            if not l2:
                while l1:
                    sortList.append( l1.val )
                    l1 = l1.next
                break

            if l1.val < l2.val:
                sortList.append( l1.val )
                l1 = l1.next
            else:
                sortList.append( l2.val )
                l2 = l2.next
        try:
            head = ListNode( sortList[0] )
            point = head
            for index in range( 1, sortList.__len__() ):
                point.next = ListNode( sortList[ index ] )
                point = point.next
        except:
            head = None

        return head
        
