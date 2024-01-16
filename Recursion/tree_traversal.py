from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
#root = TreeNode(3, TreeNode(9, TreeNode(1), None), TreeNode(20, TreeNode(15, TreeNode(16), TreeNode(13)), TreeNode(7,TreeNode(4, TreeNode(3), TreeNode(2)), TreeNode(1))))
root = TreeNode(2, TreeNode(3, TreeNode(7), TreeNode(6)), TreeNode(4, TreeNode(10), TreeNode(13)))

def sub_process(num:int):
    print(num)
    
def recursive_traversal(node):
    if node is None:
        return
    
    recursive_traversal(node.left)
    recursive_traversal(node.right)
    sub_process(node.val)
    
    
  


x = recursive_traversal(root)