1. What is a Linked List?
Learn:
Definition
Why Linked Lists exist
Difference from arrays
Nodes
Head pointer
Dynamic memory concept
Advantages
Disadvantages
    - A linked list is a linear data structure where elements are not stored in contiguous (neighboring) memory locations. Instead, each element is a separate object, called a node, which contains data and a pointer (or reference) that links to the next node in the sequence.
2. Types of Linked Lists
Understand:
Singly Linked List
Doubly Linked List
Circular Linked List
Circular Doubly Linked List
Know when each type is used.

    - 1. Singly Linked ListA Singly Linked List is the simplest type of linked list where each node contains data and a single pointer pointing to the next node in the sequence. The final node points to NULL, marking the end of the list.Direction: Forward-only traversal.Memory Cost: Minimal pointer overhead (1 pointer per node).When to use:When memory space is highly constrained.When you only need to look at data from front to back (e.g., implementing basic single-direction Stacks or Queues).For simple dynamic collections where you only insert/delete at the beginning.
    2. Doubly Linked ListA Doubly Linked List (DLL) expands on the singly list by adding a second pointer to every node. Each node contains data, a pointer to the next node, and a pointer to the previous node.Direction: Bidirectional traversal (forward and backward).Memory Cost: Higher pointer overhead (2 pointers per node).When to use:When you need to navigate back and forth frequently (e.g., the "Forward" and "Back" button history on web browsers).When you need to delete a node efficiently without traversing the whole list to find its predecessor.Used internally for implementing complex data structures like LRU (Least Recently Used) Caches.
    3. Circular Linked ListA Circular Linked List can be singly or doubly linked, but its defining feature is that the last node points back to the first node (head) instead of pointing to NULL. This creates an endless loop.Direction: Forward-only (if singly circular) but loops indefinitely.Memory Cost: Low (same pointer overhead as a standard singly linked list).When to use:When elements must be accessed in a continuous, repeating loop.Operating system process scheduling (e.g., Round-Robin Scheduling where each application gets equal CPU time slices sequentially).Multiplayer board games where turn control naturally cycles back to the first player after the last player finishes.
    4. Circular Doubly Linked ListA Circular Doubly Linked List combines the structural benefits of both worlds. Each node has next and previous pointers, the last node's next points to the head, and the head's previous points to the last node.Direction: Endless bidirectional loop.Memory Cost: Highest pointer overhead.When to use:When you need continuous, repeating navigation in both directions.Media playlists (e.g., music or video streaming apps) where skipping "Previous" on the first song jumps to the last song, and hitting "Next" on the last song loops back to the first.Advanced window managers or tabs cycling operations (like pressing Alt + Tab or Cmd + Tab to cycle backward and forward through active applications)

3. Linked List Operations
Study how to:
Traverse
Insert at beginning
Insert at end
Insert in middle
Delete
Search
Reverse (concept only)
    - Class SetupBefore performing operations, you must define the building blocks: a Node class and a LinkedList class.pythonclass Node:
    def __init__(self, data):
        self.data = data  # Stores the value
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Points to the first node
Use code with caution.1. TraverseTo traverse a list, start at the head and visit each node sequentially using a loop until you reach None.pythondef traverse(self):
    current = self.head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
Use code with caution.2. Insert at BeginningCreate a new node, point its next to the current head, and then update the head to be this new node.pythondef insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head  # Link new node to current first node
    self.head = new_node       # Move head to point to new node
Use code with caution.3. Insert at EndTraverse to the final node of the list, then point that final node's next to the new node. If the list is empty, make it the head.pythondef insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:      # If list is empty
        self.head = new_node
        return
        
    current = self.head
    while current.next is not None:  # Traverse to the last node
        current = current.next
    current.next = new_node    # Link last node to new node
Use code with caution.4. Insert in Middle (After a Target Node Value)Find the specific node you want to insert after. Point the new node's next to the target node's next, then point the target node's next to the new node.pythondef insert_after_value(self, target_data, data):
    current = self.head
    while current is not None and current.data != target_data:
        current = current.next
        
    if current is None:
        print("Target node not found.")
        return
        
    new_node = Node(data)
    new_node.next = current.next  # Link new node to the rest of the list
    current.next = new_node       # Link current node to new node
Use code with caution.5. Delete (By Value)Locate the node to delete while keeping track of the previous node. Change the previous node's next pointer to bypass the deleted node entirely.pythondef delete_value(self, key):
    current = self.head
    previous = None

    # Case 1: The head node holds the key to be deleted
    if current is not None and current.data == key:
        self.head = current.next  # Move head to next node
        return

    # Case 2: Search for the key to be deleted
    while current is not None and current.data != key:
        previous = current
        current = current.next

    # Case 3: Key was not present in the linked list
    if current is None:
        print("Value not found.")
        return

    # Unlink the node from the linked list
    previous.next = current.next
Use code with caution.6. SearchTraverse the list and check if any node's data matches your target value. Return True if found, False otherwise.pythondef search(self, target):
    current = self.head
    while current is not None:
        if current.data == target:
            return True  # Value found
        current = current.next
    return False        # Value not found
Use code with caution.7. Reverse (Concept Only)Reversing a linked list changes the direction of all the pointers. Instead of pointing to the next node, every node is updated to point to its previous node.To achieve this without losing the rest of the list, you must keep track of three pointers at the same time during a single traversal:current: The node you are currently modifying.prev: The node that came before current (initially None). You redirect current.next to point here.next_node: A temporary pointer used to remember the rest of the list before you break the link in current.The Workflow:You save the upcoming node (next_node), flip the current pointer backward (current.next = prev), shift the prev step up to current, and advance current to next_node. Once you reach the end, you update the head pointer to point to the very last node you processed (prev).

4. Arrays vs Linked Lists
Create a comparison table covering:
Memory layout
Random access
Insertions
Deletions
Cache locality
Memory usage
Best use cases
    -


| Comparison Feature | Arrays | Linked Lists |
|---|---|---|
| Memory Layout | Contiguous memory blocks allocation | Non-contiguous memory blocks allocation |
| Random Access | Supported via index calculation (O(1)) | Not supported requires sequential scan (O(n)) |
| Insertions | Slow due to element shifting (O(n)) | Fast requires updating pointers (O(1)) |
| Deletions | Slow due to element shifting (O(n)) | Fast requires updating pointers (O(1)) |
| Cache Locality | Excellent due to spatial data contiguity | Poor due to scattered node locations |
| Memory Usage | Fixed size size adjustments require reallocation | Dynamic size but adds pointer memory overhead |
| Best Use Cases | Fixed datasets requiring frequent lookups | Dynamic datasets requiring constant modifications |

5. Time Complexity Review
Write the complexities for:
Operation	Array	Linked List
Access		
Search		
Insert Beginning		
Insert End		
Delete Beginning		
Delete End		

Explain why the complexities differ.
    - 
    Time Complexity Comparison TableOperationArray (Fixed-Size / Static)Singly Linked ListAccess\(O(1)\)\(O(n)\)Search\(O(n)\) (or \(O(\log n)\) if sorted)\(O(n)\)Insert Beginning\(O(n)\)\(O(1)\)Insert End\(O(1)\) (assuming space is available)\(O(n)\) (or \(O(1)\) with a tail pointer)Delete Beginning\(O(n)\)\(O(1)\)Delete End\(O(1)\)\(O(n)\) (even with a tail pointer)Why the Complexities DifferThe differences in time complexity stem entirely from how data is physically arranged in your computer's memory and how elements are linked together.1. Accessing Elements (\(O(1)\) vs \(O(n)\))Array (\(O(1)\)): Arrays use a contiguous block of memory. Because every element is the exact same size and packed side-by-side, the computer can instantly calculate the precise memory address of any index using a simple math formula: Address = BaseAddress + (Index * ElementSize).Linked List (\(O(n)\)): Nodes are scattered randomly across your memory. The only way to find the \(5^{\text{th}}\) element is to physically start at the head and follow the pointers from node to node five times. You cannot jump directly to a specific position.2. Operations at the Beginning (\(O(n)\) vs \(O(1)\))Array (\(O(n)\)): Index 0 is locked to the very first slot of the memory block. If you want to insert a new element at the beginning, or delete the first element, every single remaining element in the array must be shifted over by one slot to clear space or close the gap.Linked List (\(O(1)\)): There is no shifting. To insert, you simply create a new node, point its next pointer to the current head, and make it the new head. To delete, you just point the head to head.next. The rest of the list remains entirely untouched.3. Operations at the EndArray (\(O(1)\)): If the array has allocated, unused slots at the end, adding or removing the final element takes exactly one step because you know its exact location and no other elements need to shift.Linked List (\(O(n)\) or \(O(1)\)):Insert End: Without a reference to the end of the list, you must traverse all \(n\) nodes to find the final node (\(O(n)\)). However, if your linked list maintains a dedicated tail pointer, you can jump straight to the end and insert in \(O(1)\) time.Delete End: Even if you have a tail pointer, deleting the last node in a singly linked list still takes \(O(n)\) time. This is because you must update the second-to-last node's next pointer to None, and the only way to reach that second-to-last node is to traverse the entire list from the beginning. (Note: A Doubly Linked List solves this by using the prev pointer, making it \(O(1)\)).

