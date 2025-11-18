class Node:
    def __init__(self,val):
        self.val = val
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)

n1.next=n2
n2.next=n3
n3.next=n4

head=n1
new_node=Node(50)
new_node.next=head
head=new_node

current=head

while current is not None:
    print(current.val,end="=>")
    current = current.next
print(None)
