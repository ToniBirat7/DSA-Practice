class Node:
    def __init__(self,value) -> None:
        self.data = value
        self.next = None
        
class LL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.n = 0

    def increament(self):
        self.n += 1
    
    def append_begging(self,value):
        new_node = Node(value)
        if self.head is None:
            self.tail = self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.increament()

    def append_last(self,value):
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.increament()

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

ll1 = LL()

ll1.append_last(1)

ll1.append_last(2)

ll1.append_last(3)

ll1.traverse()
