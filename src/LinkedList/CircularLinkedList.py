class Node :
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class  Circular_LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data=data)
        if not self.head:
            self.head = node
            node.next = self.head
            return
        curr = self.head
        node.next = curr
        while curr.next != self.head:
            curr = curr.next
        curr.next = node
        node.next = self.head
        self.head = node


    def insert_at_end(self, data):
        node = Node(data=data)
        if self.head is None:
            self.head = node
            node.next = self.head
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        node.next = self.head
        curr.next = node


    def display(self):
        if not  self.head:
            print("Empty List")
            return
        curr =self.head
        while True:
            print(f"[{curr.data}|m({curr.next.data})]", end="->")
            curr = curr.next
            if curr.next == self.head:
                break
        print(f"[{curr.data}|m({curr.next.data})]")


circularLL = Circular_LinkedList()
circularLL.insert_at_start(6)
circularLL.display()
circularLL.insert_at_end(1)
circularLL.display()
circularLL.insert_at_end(2)
circularLL.display()
circularLL.insert_at_start(7)
circularLL.display()
circularLL.insert_at_end(3)
circularLL.display()
circularLL.insert_at_end(4)
circularLL.display()
circularLL.insert_at_start(5)
circularLL.display()