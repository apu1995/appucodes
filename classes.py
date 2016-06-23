#classes in python

class greeter(object):

	def __init__ (self, name):
		self.name=name

	def greet(self, loud=False):
		if loud:
			print 'Hello %s' % self.name.upper()
		else:
			print 'Hello %s' % self.name

g=greeter('Apurva')

g.greet(loud=True)
g.greet()
print 'Made my first Python Class.'