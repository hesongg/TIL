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


def get_linked_list_sum(linked_list_1, linked_list_2):
    node1 = linked_list_1.head
    node2 = linked_list_2.head

    first_num = str(node1.data)
    second_num = str(node2.data)

    while node1.next is not None:
        first_num += str(node1.next.data)
        node1 = node1.next
    while node2.next is not None:
        second_num += str(node2.next.data)
        node2 = node2.next

    return int(first_num) + int(second_num)


def get_linked_list_sum_v2(linked_list_1, linked_list_2):
    sum_1 = convert_linked_list_by_num(linked_list_1)
    sum_2 = convert_linked_list_by_num(linked_list_2)
    return sum_1 + sum_2


def convert_linked_list_by_num(linked_list):
    cur = linked_list.head
    converted_num = cur.data

    # 더 할때 앞에서 구한 숫자 * 10 하여 자리 수 계산
    while cur.next is not None:
        converted_num = converted_num * 10 + cur.next.data
        cur = cur.next

    return converted_num


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum_v2(linked_list_1, linked_list_2))
