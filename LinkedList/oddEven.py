class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n6 = Node(60)
n7 = Node(70)
n8 = Node(80)
n9 = Node(90)

nodes = [n1,n2,n3,n4,n5,n6,n7,n8,n9]
for i in range(0,len(nodes)-1):
    nodes[i].next = nodes[i+1]

# head = n1
# values = []

# temp = head

# while temp:
#     values.append(temp.val)
#     if temp.next is None:
#         break
#     temp = temp.next.next

# temp = head.next
# while temp:
#     values.append(temp.val)
#     if temp.next is None:
#         break
#     temp = temp.next.next

# temp = head
# i=0
# while temp is not None:
#     temp.val = values[i]
#     print(temp.val,end='=>')
#     i+=1
#     temp = temp.next
# print(None)


head = n1
even = head
odd = head.next
odd_head = odd


while even is not None  and even.next is not None:
    even.next = odd.next
    even = even.next

    odd.next = even.next
    odd = odd.next


even.next = odd_head

temp = head

while temp is not None:
    print(temp.val,end='=>')
    temp = temp.next
print(None)

