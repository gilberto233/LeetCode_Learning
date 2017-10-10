# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        point = head
        selectPoint = None
        
        if not point.next:
            if n == 1:
                return None
        
        times = 1
        while point.next:
            if n > times:
                times += 1
            elif n == times:
                selectPoint = head
                times += 1
            elif n < times:
                selectPoint = selectPoint.next
                times += 1
            
            point = point.next
            
        if times == n:
            head = head.next
            
        try:
            selectPoint.next = selectPoint.next.next
        except: pass
            
        return head
        
