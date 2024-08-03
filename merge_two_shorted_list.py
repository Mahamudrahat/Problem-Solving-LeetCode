class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    current = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
        
        


    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    
    return dummy.next

def list_to_linkedlist(elements):
    dummy = ListNode()
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
      
    return dummy.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        
        node = node.next
    return result

# Example usage:
if __name__ == "__main__":
    # Create linked lists from the given lists
    list1 = list_to_linkedlist([1])
    list2 = list_to_linkedlist([1, 3, 4])

    # Merge the two lists
    merged_list = mergeTwoLists(list1, list2)
    
    # Convert the merged linked list back to a list to print the result
    print(linkedlist_to_list(merged_list))  # Output: [1, 1, 2, 3, 4, 4]
