def linkedListValues(head):
    values = []
    current = head 

    while current:
        values.append(current.value)
        current = current.next
    return values

def linkedListValuesRecursive(head):
    values = []
    fillValues(head, values)
    return values

def fillValues(head, values):
    if not head:
        return 
    values.append(head.value)
    fillValues(head.next, values)