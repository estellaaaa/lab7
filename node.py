class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            now = self.head
            while now.next:
                now = now.next
            now.next = new_node

    def deletion(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        now = self.head
        before = None
        while now and now.data != data:
            before = now
            now = now.next

        if now is None:
            return

        before.next = now.next

    def reversion(self):
        if self.head is None or self.head.next is None:
            return

        before = None
        now = self.head
        while now:
            next_node = now.next
            now.next = before
            before = now
            now = next_node

        self.head = before

    def display(self):
        now = self.head
        while now:
            print(now.data, end=" ")
            now = now.next
        print()


ll = LL()


ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)

ll.display()  # Output: 1 2 3 4 5


ll.deletion(3)
ll.display()  # Output: 1 2 4 5


ll.reversion()
ll.display()  # Output: 5 4 2 1
