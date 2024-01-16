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
    parent_node_max = [root.val]
    good_nodes = 1
    while len(stack) > 0:   
        node = stack.pop()
        maximum = parent_node_max.pop()
        
        if node.right is not None:
            stack.append(node.right)
            if node.right.val >= maximum:
                parent_node_max.append(node.right.val)
                good_nodes += 1
            else:
                parent_node_max.append(maximum)
                
        if node.left is not None:
            stack.append(node.left)
            if node.left.val >= maximum:
                parent_node_max.append(node.left.val)
                good_nodes += 1
            else:
                parent_node_max.append(maximum)
        
        
    return good_nodes

        #print(stack[-1].left, stack[-1].right, stack[-1].val)
root = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7,TreeNode(4, None, None), None)))

print(maxDepth(root))