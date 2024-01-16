from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return "Node(" + str(self.val) + ")"
        


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        direction = [['c', 0]]
        
        max_line = 0
        current_longest_line = 0

        while len(stack) > 0:
            node = stack.pop()
            current_path = direction.pop()
            
            current_longest_line = current_path[1]
            
            print(current_longest_line)
            max_line = max(max_line, current_longest_line)

            if node.right is not None:
                if current_path[0] == 'l':
                    direction.append(('r', current_longest_line+1))
                
                else:
                    direction.append(('r',1))
               
                stack.append(node.right)
                

            if node.left is not None:
                if current_path[0] == 'r':
                    direction.append(('l', current_longest_line+1))
                
                else:
                    direction.append(('l',1))
                
                stack.append(node.left)

        print(max_line)
        return max_line
    

root = TreeNode(3, TreeNode(9, TreeNode(4, None, TreeNode(3, None, None)), TreeNode(3,None,None)), TreeNode(10, TreeNode(5,None,TreeNode(7, None, None))))

Solution().longestZigZag(root)