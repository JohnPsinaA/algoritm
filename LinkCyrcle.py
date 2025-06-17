class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next        
            fast = fast.next.next  
            if slow == fast:      
                return True
        
        return False  
if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(2) 
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next 
    s = Solution()
    print(s.hasCycle(head)) 
    head2 = ListNode(1)
    head2.next = ListNode(2)
    s2 = Solution()
    print(s2.hasCycle(head2))
    head3 = ListNode(1)
    s3 = Solution()
    print(s3.hasCycle(head3)) 