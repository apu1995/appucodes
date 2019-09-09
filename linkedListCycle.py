class Node:
	def __init__(self,val):
		self.val=val
		self.next=None

def linkedListCycle(head):
	if head is None:
		return False
	slow=head
	fast=head.next
	while fast is not None and fast.next is not None:
		if slow==fast:
			return True
		slow=slow.next
		fast=fast.next.next

	return False

n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n6=Node(6)
n7=Node(7)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
n6.next=n7
n7.next=n2

print(linkedListCycle(n1))
n7.next=None
print(linkedListCycle(n1))
