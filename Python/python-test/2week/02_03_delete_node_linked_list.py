class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0

        while cur_index != index:
            cur = cur.next
            cur_index += 1

        return cur

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return

        prev_node = self.get_node(index - 1)
        index_node = self.get_node(index)
        next_node = index_node.next
        prev_node.next = next_node
        self.head = prev_node


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.delete_node(0)
linked_list.print_all()
