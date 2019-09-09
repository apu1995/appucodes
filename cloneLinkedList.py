class Node:
	def __init__(self,val,next=None,random=None):
		self.val=val
		self.next=next
		self.random=random

def cloneLinkedList(head):
	if head==None:
		return None

	curr=head
	# Adding a cloned node in between each of the nodes.
	while curr:
		temp=Node(curr.val)
		currNext=curr.next
		curr.next=temp
		temp.next=currNext
		curr=temp.next

	curr=head
	while curr:
		curr.next.random=curr.random
		curr.next=curr.next.next
		curr=curr.next

	

