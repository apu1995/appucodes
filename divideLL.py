class Node:
	def __init__(self,val,next=None):
		self.val=val
		self.next=next

	def printLL(self):
		if self is None:
			print("Empty")
			return
		while self:
			print(self.val,end=" ")
			print(" -> ",end=" ")
			self=self.next
		print("null\n")


def divideLL(n):
	if n==None:
		return n
	fast=n.next
	while fast is not None:
		fast=fast.next
		if fast is not None:
			fast=fast.next
		n=n.next
	newN=n.next
	n.next=None
	return newN

n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5

n1.printLL()
newN=divideLL(n1)
n1.printLL()
newN.printLL()



