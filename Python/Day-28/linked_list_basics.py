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

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            
            current = current.next
            
        
        return False
        
    def delete(self, value):
       
        current = self.head

        if current is None:
            print(f"List is empty. Cannot delete {value}.")
            return
        
        
        if value == current.data:
            self.head = current.next
            return

        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return 
            current = current.next
            
        
        print(f"Value {value} not found in the list.")
        
    def length(self):
        count = 0
        current = self.head

        
        while current is not None:
            count += 1
            current = current.next
            
        return count


ll = LinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

ll.display()

ll.insert_at_beginning(5)
ll.display() 

print("Search 20:", ll.search(20))  
print("Search 100:", ll.search(100)) 

ll.delete(20)
ll.display() 

print("Length:", ll.length()) 