class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_list(values):
    head = None
    tail = None
    for value in values:
        node = Node(value)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head

def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def find_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def remove_value(head, value):
    if head is None:
        return
    
    if head.data == value:
        return head.next

    current = head
    while current.next is not None:
        if current.next.data == value:
            current.next = current.next.next
            return head
        current = current.next

    return head

def remove_duplicates(head):
    if head is None:
        return head

    seen = {head.data}
    current = head
    while current.next is not None:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next
    return head

def count_occurrences(head, target):

    current = head
    count = 0
    while current:
        if current.data == target:
            count += 1
        current = current.next

    return count

if __name__ == "__main__":

    print("=" * 50)
    print("TEST 1: Create and Display List")
    print("=" * 50)

    head = create_list([10, 20, 30, 40, 50])
    print("Original List:")
    print_list(head)

    print("\n" + "=" * 50)
    print("TEST 2: Reverse List")
    print("=" * 50)

    reversed_head = reverse_list(head)
    print("Reversed List:")
    print_list(reversed_head)

    print("\n" + "=" * 50)
    print("TEST 3: Find Middle Node")
    print("=" * 50)

    head = create_list([10, 20, 30, 40, 50])
    middle = find_middle(head)
    print("List:")
    print_list(head)
    print("Middle Node:", middle.data)

    print("\n" + "=" * 50)
    print("TEST 4: Remove Value")
    print("=" * 50)

    head = create_list([10, 20, 30, 40, 50])
    print("Before Removal:")
    print_list(head)

    head = remove_value(head, 30)

    print("After Removing 30:")
    print_list(head)

    print("\n" + "=" * 50)
    print("TEST 5: Remove Duplicates")
    print("=" * 50)

    head = create_list([1, 1, 2, 3, 3, 4, 4, 5])
    print("Before:")
    print_list(head)

    head = remove_duplicates(head)

    print("After:")
    print_list(head)

    print("\n" + "=" * 50)
    print("TEST 6: Count Occurrences")
    print("=" * 50)

    head = create_list([5, 2, 5, 7, 5, 8, 5])

    print("List:")
    print_list(head)

    count = count_occurrences(head, 5)
    print("Occurrences of 5:", count)

    print("\n" + "=" * 50)
    print("ALL TESTS COMPLETED")
    print("=" * 50)