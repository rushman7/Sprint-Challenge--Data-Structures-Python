from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity == 0:
            self.storage.remove_from_tail()
            self.capacity += 1
            print(f"Removing 1 ")
            self.storage.add_to_tail(item)
            self.capacity -= 1
        else:
            self.storage.add_to_head(item)
            self.capacity -= 1
            print(f"Working: {self.storage.head.value}, {self.capacity}, {self.storage.length}")

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current_node = self.storage.head
        # TODO: Your code here
        while current_node.next is not None:
            list_buffer_contents.insert(0, current_node.value)
            print(list_buffer_contents)
            current_node = current_node.next
        list_buffer_contents.insert(0, current_node.value)
        print(f"Return: {list_buffer_contents}")
        return list_buffer_contents

# ----------------Stretch Goal-------------------
# f - e - d - c - b
# ['f', 'b', 'c', 'd', 'e']
class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
