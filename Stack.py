class Stack:
	def __init__(self,capacity):
		self.capacity=capacity
		self.elements=[None]*capacity
		self.top=-1

	def isFull(self):
		return self.top==self.capacity-1

	def isEmpty(self):
		return self.top==-1

	def push(self,x):
		if self.isFull():
			return False
		else:
			self.top=self.top+1
			self.elements[self.top]=x
			return True

	def pop(self):
		if self.isEmpty():
			return None
		else:
			pop=self.elements[self.top]
			self.top=self.top-1
			return pop

	def peek(self):
		if self.isEmpty():
			return None
		else:
			return self.elements[self.top]

	def size(self):
		return self.top+1

s=Stack(5)
print(s.size())
print(s.push(1))
print(s.size())
print(s.push(2))
print(s.push(3))
print(s.peek())
print(s.size())
print(s.push(4))
print(s.push(5))
print(s.push(6))
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())


