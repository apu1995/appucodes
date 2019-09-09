class Node:
	def __init__(self,val,left=None,right=None):
		self.val=val
		self.right=right
		self.left=left


def hasPath(root,val,arr=[]):
	if root==None:
		return False
	arr.append(root)
	if root.val==val:
		return True

	if hasPath(root.left,val,arr) or hasPath(root.right,val,arr):
		return True
	arr.pop()
	return False

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
n3.right=n7

arr=[]
hasPath(n1,7,arr)
n=len(arr)
for i in range(n-1):
	print(arr[i].val," --> ",end=" ")

print(arr[n-1].val,"\n")