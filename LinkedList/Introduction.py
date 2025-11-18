class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

n1.next = n2
n2.next=n3
n3.next = n4


curr = n1
while curr is not None:
    print(curr.val,end='=>')
    curr = curr.next
print(None)



'''
Output:
10=>20=>30=>40=>None

'''