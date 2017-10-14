# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        k = 2

        firstNode = head
        prevNode = ListNode( None )
        headnode = prevNode

        while firstNode:
            lastNode = firstNode
            for _ in range( k - 1 ):
                lastNode = lastNode.next
                if not lastNode:
                    prevNode.next = firstNode
                    return headnode.next

            prevNode.next = lastNode
            leftNode = firstNode
            rightNode = firstNode.next
            leftNode.next = lastNode.next
            for _ in range( k - 1 ):
                link = rightNode.next
                rightNode.next = leftNode
                leftNode = rightNode
                rightNode = link

            prevNode = firstNode
            firstNode = link
            lastNode = firstNode

        return headnode.next
