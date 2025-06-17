class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    class Solution(object):
        def deleteNode(self, node):
            """
            :type node: ListNode
            :rtype: void Do not return anything, modify node in-place instead.
            """
            if node is None or node.next is None:
                return
            node.val = node.next.val
            node.next = node.next.next
if __name__ == "__main__":
    head = [ListNode(4), ListNode(5), ListNode(1), ListNode(9)]
    head[0].next = head[1]
    head[1].next = head[2]
    head[2].next = head[3]
    node_to_delete = head[2] 
    s = ListNode.Solution()
    s.deleteNode(node_to_delete)
    current = head[0]
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
