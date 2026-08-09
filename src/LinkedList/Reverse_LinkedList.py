"""
Reverse the Linked_List

input  = 10->20->30->40->None
output = 40->30->20->10->None
"""
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data=data)
        if self.head is None:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end="->")
            curr = curr.next
        print(curr)


def reverse_linked_list(list):
    if list.head is None:
        return None
    if list.head.next is None:
        return list.head

    curr = list.head
    temp =  Node(0)
    prev = None

    while curr:
        temp.next = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        curr = curr.next


    return prev


def reverse_linkedlist(list):
    curr = list.head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


def reverse_list_recursive(head):
    if not head or not head.next:
        return head
    next_node = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return next_node



ll = Linked_List()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.display()
#result = reverse_linked_list(ll)
#result2= reverse_linkedlist(ll)
result3 = reverse_list_recursive(ll.head)
#print(result.data, result.next.data, result.next.next.data, result.next.next.next.data)
def display(list):
    curr = list
    while curr:
        print(curr.data, end="->")
        curr = curr.next
    print(curr)

#display(list=result)
display(list=result3)