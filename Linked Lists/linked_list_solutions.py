
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


    # 143. Reorder List / Medium / 37 minutes / (https://leetcode.com/problems/reorder-list/)
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Get first and second half of LL with slow and fast pointer
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        # Reverse second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp # second half at null, prev set to last node

        # merge two halfs 
        first,second = head, prev 
        # second half may be shorter
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next =  temp1
            first = temp1
            second = temp2

    # 19. Remove Nth Node From End of List / Medium / 27 minutes / (https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two pointers
        dummy = ListNode(0, head)
        first, second = dummy, head
        for i in range(n):
            if second:
                second = second.next
        while second:
            first = first.next
            second = second.next
        print(first, second)
        first.next = first.next.next
        return dummy.next # in case you have to remove head of node, dummy.next will always point to the head of the LL

        
    # 138. Copy List with Random Pointer / Medium / 36 minutes / (https://leetcode.com/problems/copy-list-with-random-pointer/)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Two Passes
        # Node Creation, then Linkage
        hash_copy = { None: None }
        cur = head
        # Node Creation
        while cur:
            hash_copy[cur] = Node(cur.val)
            cur = cur.next
        
        # Linkage
        cur = head
        while cur:
            copy = hash_copy[cur]
            copy.next = hash_copy[cur.next]
            copy.random = hash_copy[cur.random]
            cur = cur.next

        return hash_copy[head]

    # 2. Add Two Numbers / Medium / 46 minutes / (https://leetcode.com/problems/add-two-numbers/)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Need Carry
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            carry = val // 10 
            val = val % 10
            cur.next = ListNode(val)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
        return dummy.next

    # 141. Linked List Cycle / Easy / 20 minutes / (https://leetcode.com/problems/linked-list-cycle/)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head 
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

        