class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def insert_at_end(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            return
        
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newnode

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" --> ")
            current = current.next
        print("null")

    def delete_first(self):
        if self.head is None:
            return
        self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def delete_value(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next


    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            
            current = current.next
            
        
        return False
    
    def length(self):
        count = 0
        current = self.head

        
        while current is not None:
            count += 1
            current = current.next
            
        return count