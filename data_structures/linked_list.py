class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self._size += 1

    def remove(self, target):
        previous = None
        current = self.head

        while current is not None:
            if current.data == target:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                self._size -= 1
                return True
            previous = current
            current = current.next

        return False

    def find(self, predicate):
        current = self.head
        while current is not None:
            if predicate(current.data):
                return current.data
            current = current.next
        return None

    def to_list(self):
        return list(self)

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __len__(self):
        return self._size

    def is_empty(self):
        return self.head is None
