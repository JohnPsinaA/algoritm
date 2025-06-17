class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return None
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next        
            fast = fast.next.next  

            if slow == fast:      
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(6) 
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-3)
    head.next.next.next.next = head.next
    s = Solution()
    cycle_node = s.detectCycle(head)
    print(cycle_node.val if cycle_node else "No cycle") 
    head2 = ListNode(7)
    head2.next = ListNode(2)
    head2.next.next = head2
    s2 = Solution()
    cycle_node2 = s2.detectCycle(head2)
    print(cycle_node2.val if cycle_node2 else "No cycle")
    head3 = ListNode(0)
    s3 = Solution()
    cycle_node3 = s3.detectCycle(head3)
    print(cycle_node3.val if cycle_node3 else "No cycle")