class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

n1.next = n2
n2.next=n3
n3.next = n4


head=n1
slow = head
fast = head

while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next

print(slow.val)
   



  

