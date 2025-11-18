class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)


nodes=  [n1,n2,n3,n4,n5]

for i in range(0,len(nodes)-1):
    nodes[i].next = nodes[i+1]


head=n1
pos=2
count=0
prev_node = None
current = head

while current is not None and count<pos:
    count+=1
    prev_node = current
    current = current.next

prev_node.next = current.next

while head is not None:
    print(head.val,end='=>')
    head = head.next
print(None)



