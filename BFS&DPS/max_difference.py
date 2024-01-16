from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return "Node(" + str(self.val) + ")"
        


def maxDepth(root: Optional[TreeNode]):
    
    stack = [root]
    parent = []
    maximum = 0
    
    while len(stack) > 0:   
        node = stack.pop()
        
        if node.right is not None:
            stack.append(node.right)
            maximum = max(maximum, abs(parent[-1]-node.right.val))
            
                
        if node.left is not None:
            stack.append(node.left)
            maximum = max(maximum, abs(parent[-1]-node.left.val))
            
        elif not node.left and not node.right:
            parent.pop()   
        print(maximum, parent)
        
root = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7,TreeNode(4, None, None), None)))   
#root = TreeNode(1, None, TreeNode(2, None, TreeNode(0, TreeNode(3, None, None), None)))


maxDepth(root)  