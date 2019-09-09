class Node:
	def __init__(self,val,left=None,right=None):
		self.val=val
		self.left=left
		self.right=right

def leftView(node,level=1,maxVal=[0]):
	if node==None:
		return
	if level>maxVal[0]:
		print(node.val,end=" ")
		maxVal[0]=level
	leftView(node.left,level+1,maxVal)
	leftView(node.right,level+1,maxVal)

def rightView(node,level=1,maxVal=[0]):
	if node==None:
		return
	if level>maxVal[0]:
		print(node.val,end=" ")
		maxVal[0]=level
	rightView(node.right,level+1,maxVal)
	rightView(node.left,level+1,maxVal)

def printLine(root,i,hd=0):
	if root==None:
		return
	if hd==i:
		print(root.val,end=" ")
	printLine(root.left,i,hd-1)
	printLine(root.right,i,hd+1)


def findMinMax(root,min_max=[0,0],hd=0):
	if root==None:
		return
	if min_max[0]>hd:
		min_max[0]=hd
	elif min_max[1]<hd:
		min_max[1]=hd
	findMinMax(root.left,min_max,hd-1)
	findMinMax(root.right,min_max,hd+1)

	return min_max

def VerticalOrderTraversal(root):
	if root==None:
		return
	min_max=findMinMax(root)
	for i in range(min_max[0],min_max[1]+1):
		printLine(root,i)
		print("\n")



root = Node(12) 
root.left = Node(10) 
root.right = Node(20) 
root.right.left = Node(25) 
root.right.right = Node(40) 

leftView(root)
print("\n")
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8) 
rightView(root)

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8) 
root.right.right.right = Node(9) 

print("\n")
VerticalOrderTraversal(root)
