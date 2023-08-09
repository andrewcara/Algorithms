class Node:
    def __init__(self, data = None, next_node = None) -> None:
        self.data = data
        self.next_node = next_node
        

class LinkedList:
    
    def __init__(self, head = None) -> None:
        self.head = head
        
    def insert(self, data) -> None:
        
       node = Node(data, self.head)
       self.head = node

    def nextNode(self) ->None:
        
        itr = self.head
        if not itr:
            print("List is Empty")
        
        while itr:
            print(itr.data)
            itr = itr.next_node
        

newList = LinkedList()

#newList.insert(newNode)
newList.insert(1)
newList.insert(2)
newList.insert(3)
newList.insert(4)
newList.insert(5)

reverseLinkedList = LinkedList()


itr = newList.head
while itr:
    reverseLinkedList.insert(itr.data)
    itr = itr.next_node



newList.nextNode()
reverseLinkedList.nextNode()