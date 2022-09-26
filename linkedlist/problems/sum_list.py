def sum_list_recursive(head):
    # time complexity: O(n)
    # space complexity: O(n)
    if not head:
        return 0
    return head.value + sum_list_recursive(head.next)

def sum_list(head):
    # time complexity: O(n)
    # space complexity: O(1)
    total = 0
    current = head

    while current:
        total += current.value
        current = head.next
    return total 
