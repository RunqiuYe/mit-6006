class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        node = Doubly_Linked_List_Node(x)
        node.next = self.head
        if self.head:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node

    def insert_last(self, x):
        ###########################
        # Part (a): Implement me! #
        ###########################
        node = Doubly_Linked_List_Node(x)
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def delete_first(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        assert self.head
        x = self.head.item
        self.head = self.head.next
        if not self.head:
            self.tail = None
        else:
            self.head.prev = None
        return x

    def delete_last(self):
        x = None
        ###########################
        # Part (a): Implement me! #
        ###########################
        assert self.tail
        x = self.tail.item
        self.tail = self.tail.prev
        if not self.tail:
            self.head = None
        else:
            self.tail.next = None
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        ###########################
        L2.head = x1
        L2.tail = x2
        prev_node = x1.prev
        next_node = x2.next
        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node
        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node
        L2.head.prev = None
        L2.tail.next = None
        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        ###########################
        if not L2.head:
            return
        
        next_node = x.next
        x.next = L2.head
        L2.head.prev = x
        L2.tail.next = next_node
        if next_node:
            next_node.prev = L2.tail
        else:
            self.tail = L2.tail
        L2.head = L2.tail = None
