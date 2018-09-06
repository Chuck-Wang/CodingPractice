# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        lastnode = None
        while head.next:
            newnode = ListNode(head.val)
            newnode.next = lastnode
            lastnode = newnode
            head = head.next
        newnode = ListNode(head.val)
        newnode.next = lastnode
        return newnode
