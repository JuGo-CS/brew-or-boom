from lab1 import Array, SLLNode

class ArrayQueue:
    def __init__(self,capacity=10):
        # NOTE: DO NOT EDIT THIS CODE
        # constructor param: array capacity
        # example: queue = ArrayQueue(10)
        # set properties: array, size
        self.array = Array(capacity)
        self.size = 0

    def __repr__(self):
        # NOTE: DO NOT EDIT THIS CODE
        # string representation of ArrayQueue object
        display = ', '.join(str(self.array[i]) for i in range(self.size))
        return 'front [' + display + ']'

    def is_empty(self):
        # NOTE: DO NOT EDIT THIS CODE
        # check if queue is empty
        return self.size == 0

    def enqueue(self,item):
        # expand if array is full (use capacity property)
        if self.size == self.array.capacity:
            # double capacity (or at least increase by 1 if capacity was 0)
            new_cap = self.array.capacity * 2 if self.array.capacity > 0 else 1
            self.array.expand(new_cap)

        # place new item at the back (index = size)
        self.array[self.size] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Empty queue: cannot dequeue')

        # remove front item (index 0)
        item = self.array[0]

        # shift everything left by one
        for i in range(1, self.size):
            self.array[i-1] = self.array[i]

        # optional: clear the now-unused slot at the end
        self.array[self.size-1] = None

        self.size -= 1
        return item

    def front(self):
        if self.is_empty():
            raise Exception('Empty queue: no front')
        return self.array[0]


class SLLQueue:
    def __init__(self):
        # NOTE: DO NOT EDIT THIS CODE
        # constructor: set properties head_node, tail_node, size
        self.head_node = None
        self.tail_node = None
        self.size = 0

    def __repr__(self):
        # NOTE: DO NOT EDIT THIS CODE
        # string representation of SLLQueue object
        display = []
        node = self.head_node 
        while node != None:
            display.append(str(node.get_item()))
            node = node.get_next()
        display = ', '.join(display)
        return 'front [' + display + ']'

    def is_empty(self):
        # NOTE: DO NOT EDIT THIS CODE
        # check if queue is empty
        return self.size == 0

    def enqueue(self,item):
        new_node = SLLNode(item)

        if self.is_empty():
            # first item: head and tail point to the new node
            self.head_node = new_node
            self.tail_node = new_node
        else:
            # attach new node after tail and update tail
            self.tail_node.set_next(new_node)
            self.tail_node = new_node

        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Empty queue: cannot dequeue')

        # take item from head
        item = self.head_node.get_item()
        old_head = self.head_node

        # move head to next
        self.head_node = old_head.get_next()

        # remove link from old head
        old_head.set_next(None)

        self.size -= 1

        # if queue is now empty, reset tail as well
        if self.size == 0:
            self.head_node = None
            self.tail_node = None

        return item

    def front(self):
        if self.is_empty():
            raise Exception('Empty queue: no front')
        return self.head_node.get_item()
