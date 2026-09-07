# --- Singly Linked List ---
class SinglyNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = SinglyNode(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = SinglyNode(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = SinglyNode(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = SinglyNode(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = SinglyNode(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Index is out of range")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Index is out of range")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = SinglyNode(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        listr = ""
        while itr:
            listr += str(itr.data) + "-->"
            itr = itr.next
        print(listr)


# --- Doubly Linked List ---
class DoublyNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        listr = ""
        while itr:
            listr += str(itr.data) + "-->"
            itr = itr.next
        print(listr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.get_last_node()
        listr = ""
        while itr:
            listr += str(itr.data) + "<--"
            itr = itr.prev
        print(listr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def insert_at_beginning(self, data):
        node = DoublyNode(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = DoublyNode(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = DoublyNode(data, None, itr)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = DoublyNode(data_to_insert, self.head.next, self.head.prev)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                node = DoublyNode(data_to_insert, itr.next, itr.prev)
                itr.next = node
                break
            itr = itr.next

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Index is out of range")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Index is out of range")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = DoublyNode(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1


if __name__ == "__main__":
    # sll = SinglyLinkedList()
    # sll.insert_values(["banana", "mango", "grapes", "orange"])
    # sll.print()
    # sll.insert_after_value("mango", "apple")
    # sll.print()
    # sll.remove_by_value("orange")
    # sll.print()

    dll = DoublyLinkedList()
    dll.insert_values(["banana", "mango", "grapes", "orange"])
    dll.print_forward()
    dll.print_backward()
    dll.insert_at_beginning("apple")
    dll.print_forward()
    dll.insert_after_value("banana", "cherry")
    dll.print_forward()
    print(dll.get_length())
    dll.remove_at(2)
    dll.print_forward()
    dll.remove_by_value("grapes")
    dll.print_forward()
    dll.insert_at(2, "cherry")
    dll.print_forward()
