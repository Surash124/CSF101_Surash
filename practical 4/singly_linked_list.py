#create node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a linked list
class LinkedList:
    def __init__(self):
        self.head = None

# Append a new node
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)) + " -> None")
    #Implement the insert mrthod
    def insert(self, data,position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of bounds")
            current = current.next
        new_node.next = current.next
        current.next = new_node
    #Implement the delete method
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    #Implement the search method
    def seearch(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1
    
    #Implement the reverse method
    def reverse(self):
        prev = None 
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        
#Test the append method
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
#Implement the display method
ll.display()
#Test the insert method
ll.insert(4, 1)
ll.display()
#Test the delete method
ll.delete(2)
ll.display()
#Test the search method
print(ll.seearch(4))
print(ll.seearch(5))
#Test the reverse method
ll.reverse()
ll.display()