class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node


    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
        node.prev = curr

    def remove_at_start(self):
        if self.head is None:
            return
        else:
            curr = self.head
            if curr.next:
                self.head = curr.next
                self.head.prev = None

    def remove_at_end(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
            return
        else:
            curr = self.head
            while curr.next and curr.next.next:
                curr = curr.next
            curr.next = None
            #print(curr.next.data)





    def display(self):
        curr = self.head
        while curr:
            prev_val = curr.prev.data if curr.prev else 'None'
            next_val = curr.next.data if curr.next else 'None'
            print(f"m({prev_val})|{curr.data}|m({next_val})", end='<-->')
            curr = curr.next
        print("")


doublyLL = DoublyLinkedList()
doublyLL.remove_at_start()
doublyLL.remove_at_end()
doublyLL.insert_at_end(1)
#doublyLL.remove_at_end()
#doublyLL.display()
doublyLL.insert_at_end(2)
#doublyLL.remove_at_end()
doublyLL.display()
doublyLL.insert_at_end(3)
doublyLL.insert_at_end(4)
doublyLL.insert_at_start(5)
doublyLL.display()
doublyLL.remove_at_start()
doublyLL.display()
doublyLL.insert_at_start(6)
doublyLL.remove_at_end()
doublyLL.display()
doublyLL.insert_at_end(7)
doublyLL.display()
doublyLL.remove_at_end()
doublyLL.display()