class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_begin(self, data):
        node = Node(data=data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
            current_node = self.head


    def insert_at_end(self, data):
        node = Node(data=data)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        current_node = self.tail
        current_node.next = node
        self.tail = current_node.next


    def insert_at_position(self, data, index):
        if index == 0:
            self.insert_at_begin(data=data)
            return
        pos = 1
        current_node = self.head
        while pos != index and current_node is not None:
            pos += 1
            current_node = current_node.next
        if current_node:
            node = Node(data=data)
            node.next  = current_node.next
            current_node.next = node
        else:
            print("Index is not present")

    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node.next and current_node.next.next:
            current_node = current_node.next
        current_node.next = None
        self.tail = current_node

    def remove_node(self, data):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        previous_node = self.head
        while current_node.data != data and current_node.next:
            previous_node = current_node
            current_node = current_node.next
            #print(previous_node.data, current_node.data)
        previous_node.next = current_node.next

    def remove_node_at_index(self, index):
        if self.head is None:
            return
        if index == 0 :
            self.remove_first_node()
            return

        pos = 1
        current_node = self.head

        while pos < index and current_node:
            pos +=1
            current_node = current_node.next

        if current_node is None or current_node.next is None:
            print("Index not present")
        else:
            current_node.next = current_node.next.next


    def size_of_LL(self):
        size = 0
        current_node = self.head
        while current_node:
            size = size + 1
            current_node = current_node.next
        return size

    def display(self):
        current = self.head
        while current:
            print(current.data, end="-> ")
            current = current.next
        print("None")



l1 = LinkedList()
l1.insert_at_end(10)
l1.insert_at_begin(90)
print(l1.head.data, l1.tail.data)
l1.insert_at_end(30)
l1.display()
print(l1.head.data, l1.tail.data)
l1.insert_at_position(60,1)
print(l1.head.data, l1.tail.data)
l1.display()
l1.insert_at_end(100)
l1.insert_at_begin(40)
l1.insert_at_begin(50)
l1.display()
print(l1.head.data, l1.tail.data)
l1.insert_at_begin(80)
l1.remove_first_node()
l1.insert_at_end(70)
l1.remove_last_node()
print(l1.head.data, l1.tail.data)

#print(l1)
#l1.display()