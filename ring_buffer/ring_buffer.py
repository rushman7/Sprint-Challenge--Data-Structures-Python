from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity == self.storage.length: # check if capacity is reached
            self.current.value = item # assign new value to be the current
            if self.current is self.storage.tail: # if current is tail(end)
                self.current = self.storage.head # current becomes start head
            else:
                self.current = self.current.next # move to next
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.head

    def get(self):
        list_buffer_contents = []
        current_node = self.storage.head

        while current_node:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------

# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
