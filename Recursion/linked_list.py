class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
node1 = ListNode(1)
node2 = ListNode(8)
node3 = ListNode(10)

node1.next=node2
node2.next=node3


def recursive_linked_list_sum(node: ListNode) ->int:   
    if node.next is None:
        return node.val
    else:
        return node.val + recursive_linked_list_sum(node.next)
    


x = recursive_linked_list_sum(node1)

print(x)