class Queue:
	def __init__(self,capacity):
		self.capacity=capacity
		self.elements=[None]*capacity
		self.front=0
		self.rear=self.capacity-1
		self.size=0

	def isFull(self):
		return self.size==self.capacity

	def isEmpty(self):
		return self.size==0

	def qFront(self):
		if self.isEmpty():
			return None
		else:
			return self.elements[self.front]

	def qRear(self):
		if self.isEmpty():
			return None
		else:
			return self.elements[self.rear]

	def enQueue(self,x):
		if self.isFull():
			return False
		else:
			self.rear=(self.rear+1)%self.capacity
			self.elements[self.rear]=x
			self.size=self.size+1
			return True

	def deQueue(self):
		if self.isEmpty():
			return None
		else:
			self.size=self.size-1
			popped=self.elements[self.front]
			self.front=(self.front+1)%self.capacity
			return popped

	def printQueue(self):
		print(self.elements)

q=Queue(5)
q.printQueue()
q.enQueue(1)
q.printQueue()
q.enQueue(2)
q.printQueue()
q.enQueue(3)
q.printQueue()
q.enQueue(4)
q.printQueue()
print(q.enQueue(5))
q.printQueue()
print(q.deQueue())
print(q.enQueue(10))
q.printQueue()
