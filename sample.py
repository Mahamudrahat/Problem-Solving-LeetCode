class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        
        total = carry + x + y
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    if carry > 0:
        current.next = ListNode(carry)
    
    return dummy_head.next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

# Example usage:
l1_values = [2, 4, 3]  # You can change these values as needed
l2_values = [5, 6, 4]  # You can change these values as needed

l1 = create_linked_list(l1_values)
l2 = create_linked_list(l2_values)

result = addTwoNumbers(l1, l2)

print("Result linked list: ", end="")
print_linked_list(result)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        
        total = carry + x + y
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    if carry > 0:
        current.next = ListNode(carry)
    
    return dummy_head.next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

# Example usage:
l1_values = [2, 4, 3]  # You can change these values as needed
l2_values = [5, 6, 4]  # You can change these values as needed

l1 = create_linked_list(l1_values)
l2 = create_linked_list(l2_values)

result = addTwoNumbers(l1, l2)

print("Result linked list: ", end="")
print_linked_list(result)
