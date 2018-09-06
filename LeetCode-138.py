# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyObject(self, head):
        if head:
            x = head.label
            new = RandomListNode(x)
            new.next = head.next
            head.next = new
            newhead = new.next
            self.copyObject(newhead)
            return head
        else:
            return None

    def copyReference(self, head):
        if not head:
            return None
        if not head.next:
            return None
        else:
            if head.random:
                head.next.random = head.random.next
            else:
                head.next.random = None
            self.copyReference(head.next.next)
            return head

    def spiltList(self, head):
        if head:
            newhead = head.next
            oldhead = head
            oldhead.next = oldhead.next.next
            if newhead.next:
                newhead.next = newhead.next.next
            else:
                newhead.next = None
            self.spiltList(oldhead.next)
        else:
            return head
        return newhead, oldhead

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        self.copyObject(head)
        self.copyReference(head)
        (newhead, oldhead) = self.spiltList(head)
        return newhead