class ListNode:
    prev: Optional[ListNode]
    val: any
    nxt: Optional[ListNode]

    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.nxt = nxt


class MyLinkedList:
    head: Optional[ListNode]
    tail: Optional[ListNode]

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        cur = self.head
        it = 0

        while cur is not None:
            if it == index:
                return cur.val

            cur = cur.nxt
            it += 1

        return -1

    def addAtHead(self, val: int) -> None:
        new_list_node = ListNode(val, None, self.head)

        if self.head is None:
            self.head = new_list_node
            self.tail = new_list_node
            return

        self.head.prev = new_list_node
        self.head = new_list_node

    def addAtTail(self, val: int) -> None:
        new_list_node = ListNode(val, self.tail, None)

        if self.tail is None:
            self.head = new_list_node
            self.tail = new_list_node
            return

        self.tail.nxt = new_list_node
        self.tail = new_list_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= 0:
            self.addAtHead(val)
            return

        cur = self.head
        it = 0

        while cur is not None:
            if it == index - 1:
                if cur.nxt is None:
                    self.addAtTail(val)
                    return

                new_list_node = ListNode(val, cur, cur.nxt)

                cur.nxt.prev = new_list_node
                cur.nxt = new_list_node

                return

            cur = cur.nxt
            it += 1

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.nxt

            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None

            return

        cur = self.head
        it = 0

        while cur is not None:
            if it == index - 1:
                node_to_delete = cur.nxt

                if node_to_delete is None:
                    return

                if node_to_delete.nxt is None:
                    self.tail = cur
                    cur.nxt = None
                    return

                cur.nxt = node_to_delete.nxt
                node_to_delete.nxt.prev = cur

                return

            cur = cur.nxt
            it += 1