import math
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
node1 = ListNode(1)
node2 = ListNode(8)
node3 = ListNode(10)

node1.next=node2
node2.next=node3


i = 1
current_suml1 = l1.val * i
current_nodel1 = l1
output = []
while current_nodel1.next != None:
    i *=10
    current_nodel1 = current_nodel1.next
    current_suml1 += (current_nodel1.val * i) 

i = 1
current_suml2 = l2.val * i
current_nodel2 = l2

while current_nodel2.next != None:
    i *=10
    current_nodel2 = current_nodel2.next
    current_suml2 += (current_nodel2.val * i) 

current_sum = current_suml1 + current_suml2

for i in range((int(math.log10(current_sum))),-1,-1):
    app_number = current_sum // (1*(10**i))
    output.insert(0,app_number)
    
    current_sum -= app_number * (1*(10**i))

print(output)


        
    