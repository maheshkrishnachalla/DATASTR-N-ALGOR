class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    """def __repr__(self):
        values = []
        curr = self
        while curr:
            values.append(str(curr.data))
            curr = curr.next
        return "->".join(values)+"-> None"
        """



class Linked_List:

    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def remove_at_start(self):
        if self.head is not None:
            self.head = self.head.next

    def insert_at_end(self, data):
        node =  Node(data)
        if self.head is None:
            self.head = node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def remover_at_end(self):
        if self.head is None:
            return
        curr = self.head
        if curr.next is None:
            self.head = None
        while curr.next and curr.next.next:
            curr = curr.next
        curr.next = None

    def insert_at_index(self, p, data):
        if p == 0:
            self.insert_at_start(data)
            return
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        curr = self.head
        i= 0
        while i<p-1 and curr.next:
            curr = curr.next
            i = i+1
        node.next = curr.next
        curr.next = node

    def remove_at_index(self, idx):
        if self.head is None:
            return
        if idx==0:
            self.remove_at_start()
            return
        curr = self.head
        i = 1
        while i < idx and curr.next:
            curr = curr.next
            i+=1
        try:
            curr.next = curr.next.next
        except Exception as e:
            print(e)





    def display(self):
        curr = self.head
        while curr:
            print(f"[{curr.data}]", end="->")
            curr = curr.next
        print("None")

    def __sizeof__(self):
        size = 0
        curr = self.head
        while curr:
            size +=1
            curr =curr.next
        return size




n1= Node(5)
#print(n1.data)
#print(n1.__repr__())

l1= Linked_List()
l1.insert_at_index(0,15)
l1.display()
l1.insert_at_end(7)
l1.display()
l1.insert_at_start(9)
l1.insert_at_start(2)
l1.display()
l1.insert_at_end(8)
l1.insert_at_end(1)
l1.display()
l1.remove_at_index(0)
l1.display()
print(l1.__sizeof__())
l1.insert_at_end(10)
l1.display()
print(l1.__sizeof__())
l1.insert_at_index(1,12)
l1.display()
l1.remove_at_start()
l1.insert_at_start(4)
l1.display()
l1.insert_at_index(0,2)
l1.display()
print(l1.__sizeof__())
l1.insert_at_end(11)
l1.display()
l1.insert_at_index(6,14)
l1.display()
l1.insert_at_start(9)
l1.insert_at_end(20)
l1.display()
print(l1.__sizeof__())
