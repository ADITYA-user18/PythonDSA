class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

n1.next = n2
n2.next = n3
n3.next = n4

new_node = Node(50)
pos = 2
prev_node = None
head = n1
current = head
count=0


while current is not None and count<pos:
    count+=1
    prev_node = current
    current = current.next
prev_node.next = new_node
new_node.next = current





while head is not None:
    print(head.val,end='=>')
    head = head.next
print(None)