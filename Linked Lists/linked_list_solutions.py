
class LinkedList:
    # 206. Reverse Linked List / Easy / 7:36 minutes / (https://leetcode.com/problems/reverse-linked-list/)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative Solution
        # T O(n) M O(1)
        cur, prev = head, None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
        #################################################################
        # Recursive Solution
        def reverse(cur, prev):
            if cur is None:
                return prev
            else:
                next = cur.next
                cur.next = prev
                return reverse(next, cur)
        
        return reverse(head, None)
        
    # 21. Merge Two Sorted Lists / Easy / 15 minutes / (https://leetcode.com/problems/merge-two-sorted-lists/)
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy # Tail pointer

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next
