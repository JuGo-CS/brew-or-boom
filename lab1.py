# CMSC 123 LAB 1 - Arrays and Linked Lists

from operator import index

#-------------------------------------------- ARRAY ---------------------------------------------------------#
class Array:
	def __init__(self,capacity):
		# NOTE: DO NOT EDIT THIS CODE
		# __init__ method: constructor
		# called when creating new Array objects
		# example: a = Array(10), where capacity = 10
		self.capacity = capacity 
		self.items = []
		for i in range(capacity):		# initialize array with None items
			self.items.append(None)

	def __repr__(self):
		# NOTE: DO NOT EDIT THIS CODE
		# string representation of Array object
		# convert all items to string: 	str(x) for x in self.items
		# use a comma to separate them: ', '.join(...)
		display = ', '.join(str(x) for x in self.items)
		return '[' + display + ']' # wrap with [ ] to look like an array

	def __getitem__(self,index):
    		
		min_index = 0	#setting a minimum index to be used for the condition
		
		'''
		if index is out-of-bounds(less than min_index or greater than/equal to capacity)
		raise an error, else get value of item
		'''
		if (index < min_index or index >= self.capacity):	
			raise IndexError('Array.get: Index out of bounds')	
		return self.items[index]

	def __setitem__(self,index,item):

		min_index = 0 # setting a minimum index to be used for the condition

		''' 
		If index is out-of-bounds(less than min_index or greater than/equal to capacity)
		raise an error else, set value of item
		'''
		if (index < min_index or index >= self.capacity): 
			raise IndexError('Array.set: Index out of bounds')
		self.items[index] = item


	def expand(self,new_capacity):
		
		# New bigger array
		new_self = []

		# For loop to reassign the elements in the old array into the new array
		for i in range (new_capacity): 
			if i < self.capacity:
				new_self.append(self.items[i])
			else:
				new_self.append(None)		# append an empty element to fill the remaining slot of the new array with new capacity 

		# Updating self.items and self.capacity 
		self.items, self.capacity = new_self, new_capacity
		
#--------------------------------------------SLL NODE---------------------------------------------------------#
class SLLNode:
	def __init__(self,item=None,next_node=None):
		# NOTE: DO NOT EDIT THIS CODE
		# __init__ method: constructor
		# called when creating new SLLNode objects
		# item and next_node are optional parameters; if not set, use None
		self.item = item 
		self.next = next_node

	def __repr__(self):
		# NOTE: DO NOT EDIT THIS CODE
		# string representation of SLLNode object
		return '<SLLNode: %s>' % str(self.item)

	# Getter and Setter Methods
	# Use self.item and self.next

	def get_item(self):
    	# Get value of self.item
		return self.item 

	def set_item(self,item):
		# To set value of set.item
		self.item = item

	def get_next(self):
		# Get value of self.item
		return self.next

	def set_next(self,next_node):
		# To set value of set.next
		self.next = next_node

#--------------------------------------------DLL NODE---------------------------------------------------------#
class DLLNode:
	def __init__(self,item=None,prev_node=None,next_node=None):
		# __init__ method: constructor
		# called when creating new SLLNode objects
		# item, prev_node, next_node are optional parameters; if not set, use None
		self.item = item 
		self.prev = prev_node
		self.next = next_node

	def __repr__(self):
		# string representation of DLLNode object
		return '<DLLNode: %s>' % str(self.item)

	# Getter and Setter Methods
	# Use self.item, self.prev, and self.next

	def get_item(self):
		# Get value of self.item
		return self.item

	def set_item(self,item):
		# To set value of self.item
		self.item = item

	def get_prev(self):
		# Get value of self.prev
		return self.prev

	def set_prev(self,prev_node):
		# To set value of self.prev to prev_node
		self.prev = prev_node

	def get_next(self):
		# Get value of self.next
		return self.next

	def set_next(self,next_node):
		# To set value of self.next to next_node
		self.next = next_node
