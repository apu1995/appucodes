class Node:
	def __init__(self,val,right=None,left=None):
		self.val=val
		self.left=left
		self.right=right

def balanced(root):
	if root==None:
		return 0
	left=balanced(root.left)
	right=balanced(root.right)
	if left==-1 or right==-1:
		return -1
	if abs(left-right)>1:
		return -1
	if right>left:
		return right+1
	else:
		return left+1


n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n6=Node(6)
n7=Node(7)
n8=Node(8)

n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.left=n6
n5.right=n7
n7.right=n8

print(balanced(n1))