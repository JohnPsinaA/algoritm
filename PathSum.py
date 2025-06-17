class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return targetSum == 0
        
        targetSum -= root.val
        
        if not root.left and not root.right:
            return targetSum == 0
        return (self.hasPathSum(root.left, targetSum) or 
                self.hasPathSum(root.right, targetSum))
if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
    root.right = TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
    
    s = Solution()
    print(s.hasPathSum(root, 22)) 
    print(s.hasPathSum(root, 26))  
    print(s.hasPathSum(root, 27))  
    print(s.hasPathSum(None, 0))   
    print(s.hasPathSum(None, 1))  