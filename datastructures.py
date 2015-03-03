class Node:
	def __init__(self,initdata):
		self.data = initdata
		self.next = None
	def getData(self):
		return self.data
	def getNext(self):
		return self.next
	def setData(self,newdata):
		self.data = newdata
	def setNext(self,newnext):
		self.next = newnext

class LinkedList:
	def __init__(self):
		self.head = None
	"""
	def __init__(self,data):
		newnode = Node(data)
		self.head = newnode
	"""
	def isEmpty(self):
		return self.head is None
	def append(self,item):
		newnode = Node(item)
		if self.head is None:
			self.head = newnode
			return
		temp = self.head
		while temp.getNext() is not None:
			temp = temp.getNext()
		temp.setNext(newnode)
	def size(self):
		count = 0
		temp = self.head
		while temp is not None:
			temp = temp.getNext()
			count = count + 1
		return count
	def search(self,item):
		temp = self.head
		while (temp is not None) and (temp.getData() is not item):
			temp = temp.getNext()
		if temp is not None:
			return True
		return False
	def remove(self,item):
		if self.head.getData() is item:
			self.head = self.head.getNext()
			return
		temp = self.head
		while (temp.getNext().getData() is not item) and (temp is not None):
			temp = temp.getNext()
		if temp is None:
			print "Item not found."
			return
		temp.setNext(temp.getNext().getNext())
	def __repr__(self):
		temp = self.head
		x = []
		while temp is not None:
			x.append(str(temp.getData()))
			temp = temp.getNext()
		st = " ---> "
		return st.join(x)

class OrderedList:
	def __init__(self):
		self.head = None
	"""
	def __init__(self,data):
		newnode = Node(data)
		self.head = newnode
	"""
	def isEmpty(self):
		return self.head is None
	def add(self,item):
		newnode = Node(item)
		if self.head is None:
			self.head = newnode
			return
		temp = self.head
		while (temp.getNext() is not None) and (temp.getNext().getData() <= item):
			temp = temp.getNext()
		newnode.setNext(temp.getNext())
		temp.setNext(newnode)
	def size(self):
		count = 0
		temp = self.head
		while temp is not None:
			temp = temp.getNext()
			count = count + 1
		return count
	def search(self,item):
		temp = self.head
		while (temp is not None) and (temp.getData() is not item):
			temp = temp.getNext()
		if temp is not None:
			return True
		return False
	def remove(self,item):
		if self.head.getData() is item:
			self.head = self.head.getNext()
			return
		temp = self.head
		while (temp.getNext().getData() is not item) and (temp is not None):
			temp = temp.getNext()
		if temp is None:
			print "Item not found."
			return
		temp.setNext(temp.getNext().getNext())
	def __repr__(self):
		temp = self.head
		x = []
		while temp is not None:
			x.append(str(temp.getData()))
			temp = temp.getNext()
		st = " ---> "
		return st.join(x)

class Queue:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return len(self.items) is 0
	def enqueue(self,item):
		self.items.append(item)
	def dequeue(self):
		return self.items.pop(0)
	def size(self):
		return len(self.items)
	def __str__(self):
		return  str(self.items)

class Stack:
	def __init__(self):
		self.items = []
	def isEmpty(self):
		return len(self.items) is 0
	def push(self,item):
		self.items.append(item)
	def pop(self):
		return self.items.pop(len(self.items)-1)
	def size(self):
		return len(self.items)
	def __str__(self):
		return  str(self.items)

