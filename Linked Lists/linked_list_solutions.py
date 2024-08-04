
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
        
        