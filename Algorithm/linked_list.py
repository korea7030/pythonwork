class Node:
    def __init__(self, item):
        self.item = item  # item
        self.next = None  # next


class LinkedList:
    def __init__(self):
        self.head = None  # 첫번째 노드를 가리킴

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def next(self):
        if self.head == None:
            print("no next item")
        else:
            return self.head.item

    def printList(self):
        current = self.head

        if (current is None):
            print("Not information")
            return

        while(current is not None):
            print(current.item, end=" ")
            current = current.next

    def reverse(self):
        prev = None
        current = self.head

        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def search(self, item):
        temp = self.head
        flag = False

        while temp is not None and flag is False:
            if(temp.item == item):
                flag = True
            else:
                temp = temp.next

        if flag:
            print("find", temp.item)
        else:
            print("Not find")

    def remove(self, item):
        prev = None
        current = self.head
        flag = False

        while current is not None and flag is False:
            if (current.item == item):
                flag = True
            else:
                prev = current
                current = current.next

        if current is None:
            print("not find")
        elif prev == None:  # 노드가 한개 일때 삭제한 경우
            self.head = current.next
        else:  # None 값 대입
            prev.next = current.next

    def get_last_n_node(self, n):
        temp1 = self.head
        temp2 = self.head

        if n != 0:
            for i in range(n):
                temp2 = temp2.next

            if temp2 is None:
                return None

        while temp2.next is not None:
            temp2 = temp2.next
            temp1 = temp1.next

        return temp1.item


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.push(4)

    linked_list.printList()

    linked_list.reverse()
    linked_list.printList()

    a = linked_list.get_last_n_node(3)
    # print(a)

    # print(linked_list.next())
