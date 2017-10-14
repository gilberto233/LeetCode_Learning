# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        buffer = {}

        for headnode in range( len( lists ) ):
            if lists[ headnode ]:
                buffer[ headnode ] = lists[ headnode ].val
            else:
                pass
        if not len( buffer ):
            return

        minimum = min(buffer.values())
        for key in buffer.keys():
            if buffer[key] == minimum:
                miniIndex = key
                break
        if lists[miniIndex].next:
            lists[miniIndex] = lists[miniIndex].next
            buffer[miniIndex] = lists[miniIndex].val
        else:
            buffer.pop(miniIndex)

        head = ListNode( minimum )
        point = head

        while len( buffer ):
            minimum = min( buffer.values() )
            for key in buffer.keys():
                if buffer[ key ] == minimum:
                    miniIndex = key
                    break

            if lists[ miniIndex ].next:
                lists[ miniIndex ] = lists[ miniIndex ].next
                buffer[ miniIndex ] = lists[ miniIndex ].val
            else:
                buffer.pop( miniIndex )

            point.next = ListNode( minimum )
            point = point.next

        return head
       
