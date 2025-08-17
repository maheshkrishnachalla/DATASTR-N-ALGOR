class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        node = Node(data=data)
        node.next = self.head
        self.head = node

    def insert_at_end(self, data):
        node = Node(data=data)
        if self.head is None:
            self.head = node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node

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
print(l1.size_of_LL())
l1.insert_at_end(10)
print(l1.size_of_LL())
l1.insert_at_end(20)
l1.insert_at_end(30)
l1.insert_at_begin(40)
l1.insert_at_begin(50)
l1.insert_at_begin(60)
l1.insert_at_position(70,1)
l1.insert_at_end(80)
l1.remove_node(80)
l1.remove_node(60)
l1.display()
l1.insert_at_end(100)
l1.display()
print(l1.size_of_LL())
l1.remove_node(30)
l1.display()
l1.insert_at_begin(90)
l1.remove_last_node()
l1.remove_first_node()
l1.display()
l1.remove_node_at_index(3)
l1.display()
print(l1.size_of_LL())

#print(l1)
#l1.display()

