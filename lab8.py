from lab1 import Array, SLLNode
from classes import Entry


class HashTableSC:
    def __init__(self, capacity=20):
        self.array = Array(capacity)  
        self.size = 0  

    def __repr__(self):
        out = [] #list na inu-return later
        for i in range(self.array.capacity): #will loop sa lahat ng index
            node = self.array[i]
            chain = []
            while node != None: #let say may linked list on that index, will get everything, store sa chain list
                chain.append(f"({node.get_item().key}:{node.get_item().value})")
                node = node.get_next()
            out.append(f"{i}: " + " -> ".join(chain) + "\n")
        return "\n".join(out)

    def hash(self, key):
        total_sum = 0
        for letter in key: #adds every letter ascii value
            total_sum += ord(letter)

        return total_sum  

    def compress(self, hash_code): #make sure na ang index in with in range
        return hash_code % self.array.capacity  

    def hash_index(self, key):
        return self.compress(self.hash(key))  # Get index from hash and compress

    def get(self, key):
        index = self.hash_index(key)  # Compute hash index (gamit ang function na nasa taas)
        node = self.array[index]  

        while node != None:
            entry = node.get_item()
            if entry.key == key:
                return entry.value  # match? return lang agad ang value
            node = node.get_next()  

        return None  # let say walang laman ang array, will return None lang

    def put(self, key, value):
        index = self.hash_index(key)  # Compute hash index
        node = self.array[index]  # Start at the chain head

        # first case if may laman ang index na yan
        while node != None:
            entry = node.get_item()
            if entry.key == key:
                old_value = entry.value
                entry.value = value  # Update value
                return old_value  # Return old value
            node = node.get_next()

        # pero if wala, gagawa ng bagong entry and SLLNode
        new_entry = Entry(key, value)  # Create new entry
        new_node = SLLNode(new_entry, self.array[index])  # Create new node (ma point sa current head on that index)
        self.array[index] = new_node  # Set as new head
        self.size += 1  
        return None

    def remove(self, key):
        index = self.hash_index(key)  # Compute hash index
        node = self.array[index]  # Start in the head of that index

        # slot empty
        if node == None:
            return None  # Nothing to remove

        # CASE 1: first node matches
        if node.get_item().key == key:
            old_value = node.get_item().value
            self.array[index] = node.get_next()  # Remove head, point to next
            self.size -= 1  # Decrement size
            return old_value

        
        prev = None 
        # CASE 2: somewhere in chain
        while node != None:
            entry = node.get_item()
            if entry.key == key: # if nag same ang value nila meaning that is the node we are going to remove
                old_value = entry.value
                prev.set_next(node.get_next())  

                self.size -= 1  # Decrement size
                return old_value

            prev = node  # Update prev pointer, will point sa current na node
            node = node.get_next()  # para ang aton node ma move naman sa next node

        return None  # if walang makita na same na key, r eturn None

    def keys(self):
        counter = 0
        while counter != self.array.capacity: # will loop each index
            linklist_node = self.array[counter]
            while linklist_node != None: #check if may SLL on that index, if yes, will iterate each
                item = linklist_node.get_item()
                yield item.key  # Yield and keys
                linklist_node = linklist_node.get_next()
            
            counter += 1

    def values(self):
        counter = 0
        while counter != self.array.capacity:
            linklist_node = self.array[counter]
            while linklist_node != None:
                item = linklist_node.get_item()
                yield item.value  # Yield ang lahat na value
                linklist_node = linklist_node.get_next()
            
            counter += 1

    def entries(self):
        counter = 0
        while counter != self.array.capacity:
            linklist_node = self.array[counter]
            while linklist_node != None:
                yield linklist_node.get_item()
                linklist_node = linklist_node.get_next()
            
            counter += 1


class HashTableLP:
    def __init__(self, capacity=20):
        self.array = Array(capacity)  
        self.size = 0  
        self.slots = capacity  
        self.DELETED = "DELETED"

    def hash(self, key):
        total_sum = 0
        for letter in key: #adds every letter ascii value
            total_sum += ord(letter)
        return total_sum  

    def compress(self, hash_code): #make sure na ang index in with in range
        return hash_code % self.array.capacity  

    def hash_index(self, key):
        return self.compress(self.hash(key))  # Get index from hash and compress

    def __repr__(self):
        out = [] # list na e re-return later
        for i in range(self.array.capacity):
            cell = self.array[i]
            if cell is None:
                out.append(f"{i}: None")
            elif cell == self.DELETED:
                 out.append(f"{i}: DELETED")
            else:
                potion_name = cell.value.potion_name
                ingredients = cell.value.ingredients
                description = cell.value.description
                out.append(f"{i}: ({potion_name} : {ingredients} : {description})")
        return "\n".join(out)

    def get(self, key):
        index = self.hash_index(key)  # get the value of it's index
        index_starting = index

        while True:
            cell = self.array[index]

            if cell is None:  
                # Hitting a None means the original insertion chain ended here
                return None

            if cell == self.DELETED:
                # Skip deleted cells, continue probing
                index = (index + 1) % self.array.capacity
                if index == index_starting: 
                    return None
                continue # Go to next iteration of while loop

            # found key (and it's not deleted)
            if cell.key == key:
                return cell.value  # Return value

            index = (index + 1) % self.array.capacity #make sure that the index will be contained inside the storage

            # we looped the whole table
            if index == index_starting:
                return None  # Not found, return None

    def put(self, key, value):
        index = self.hash_index(key)  # Start at hash index
        # print(f"Key: {key} \nIndex: {index}\n")
        start_index = index

        if self.size == self.array.capacity:
            return None

        first_available_index = None # Track the first "DELETED" or "None" slot

        while True:
            cell = self.array[index]

            if cell == None:
                break # meaning we can put on that index 

            # If key exists, replace the value (must not be DELETED marker)
            if cell != self.DELETED and cell.key == key:
                old_value = cell.value
                cell.value = value  # Update value
                return old_value
            
            # save the index first (may use later) and will continue to loop (check first if there are same key value on other cell)
            if cell == self.DELETED and first_available_index == None:
                first_available_index = index
            
            index = (index + 1) % self.array.capacity
            if index == start_index:
                break 

        # If we broke the loop because we hit None, use the first available deleted slot we saw, if any
        insert_index = first_available_index 
        if first_available_index == None:
            insert_index = index
        
        # Insert into the chosen index
        self.array[insert_index] = Entry(key, value)  # Insert new entry
        self.size += 1  # Increment size
        return None


    def remove(self, key):
        index =  self.hash_index(key)  #get the index value
        index_starting = index

        while True:
            cell = self.array[index] 

            if cell is None:  
                # If we hit None, the key was never inserted
                return None

            if cell == self.DELETED:
                # Skip deleted cells during search
                index = (index + 1) % self.array.capacity
                if index == index_starting: return None
                continue

            if cell.key == key:
                old_value = cell.value
                self.array[index] = self.DELETED 
                self.size -= 1  # Decrement size
                return old_value

            # move to next slot
            index = (index + 1) % self.array.capacity  # Linear probe
            if index == index_starting:
                return None  # Not found

    def keys(self):
        # Filter out both None and deleted entries
        for cell in self.array.items:  
            if cell != None and cell != self.DELETED:  
                yield cell.key  # yield lang ang key

    def values(self):
        # Filter out both None and deleted entries
        for cell in self.array.items:  
            if cell != None and cell != self.DELETED:  
                yield cell.value  # Yield value

    def entries(self):
        # Filter out both None and deleted entries
        for cell in self.array.items:  
            if cell != None and cell != self.DELETED:  
                yield cell  # Yield entry
