Implement Priority Queue

class pQueue:
	def __init__(self,capacity=100):
		self.capacity=capacity
		self.values=[0 for _ in range(capacity)]
		self.next=0

	def heapify(self,values):
		if len(values)>capacity:
			return -1
		for x in values:
			self.insert(x)

	def insert(self,x):
		self.values[self.next]=x
		self.minHeapify(self.next)
		self.next=self.next+1

	def minHeapify(self,pos):
		if pos==0:
			return
		else:
			parent=self.getParent(pos)
			if self.values[parent]>self.values[pos]:
				self.values[pos],self.values[parent]=self.values[parent],self.values[pos]
				self.minHeapify(parent)

	def getParent(self,pos):
		return int(pos/2)

	def getLeftChild(self,pos):
		return pos*2+1

	def getRightChild(self,pos):
		return pos*2+2

	def pop(self):
		res=self.values[0]
		self.values[0],self.values[next-1]=self.values[next-1],self.values[0]
		self.next=self.next-1
		self.heapify(0)



