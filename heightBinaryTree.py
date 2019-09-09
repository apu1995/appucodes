class Node:
	def __init__(self,val,right=None,left=None):
		self.val=val
		self.left=left
		self.right=right


def height(root):
	if root==None:
		return 0
	curr=[root]
	print(curr)
	height=0
	while(curr):
		nextnodes=[]
		for n in curr:
			if n.left:
				nextnodes.append(n.left)
			if n.right:
				nextnodes.append(n.right)
		curr=nextnodes
		height=height+1

	return height

n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
n6=Node(6)
n7=Node(7)

n1.left=n2
n1.right=n3
n2.left=n4
n2.right=n5
n3.left=n6
n5.right=n7

print(height(n1))