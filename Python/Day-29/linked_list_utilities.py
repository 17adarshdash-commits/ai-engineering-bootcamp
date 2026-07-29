class Node:
    def __init__(self, value):
        self.value = value
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
        print(current.value, end=" -> ")
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
    return slow.value if slow else None


if __name__ == "__main__":
    head = create_list([10, 20, 30, 40, 50])
    print_list(head)

    middle = find_middle(head)
    print(middle)

    reversed_head = reverse_list(head)
    print_list(reversed_head)
