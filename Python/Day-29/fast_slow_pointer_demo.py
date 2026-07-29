class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, value):

        newnode = Node(value)

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
            print(current.value, end=" --> ")
            current = current.next
        print("null")

    def length(self):
        count = 0
        current = self.head

        
        while current is not None:
            count += 1
            current = current.next
            
        return count
    
    def find_middle(self):

        if not self.head:
            return None
        
        current = self.head
        slow = current
        fast = current

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    
    def has_cycle(self):

        if not self.head or not self.head.next:
            return False
    
        current = self.head

        slow = current
        fast = current

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False
    
if __name__ == "__main__":
    ll = LinkedList()

    # Insert values
    ll.insert_end(10)
    ll.insert_end(20)
    ll.insert_end(30)
    ll.insert_end(40)
    ll.insert_end(50)

    print("Linked List:")
    ll.display()

    print("\nLength:", ll.length())

    print("Middle Node:", ll.find_middle())

    print("Has Cycle:", ll.has_cycle())

    print("\n-------------------------")
    print("Even Length Test")

    ll2 = LinkedList()

    ll2.insert_end(10)
    ll2.insert_end(20)
    ll2.insert_end(30)
    ll2.insert_end(40)
    ll2.insert_end(50)
    ll2.insert_end(60)

    ll2.display()

    print("\nLength:", ll2.length())
    print("Middle Node:", ll2.find_middle())