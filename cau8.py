class LinkedList:
    def chen_tang_dtb(self, sv):
        new_node = Node(sv)
        if self.head is None or self.head.data.dtb >= sv.dtb:
            new_node.next = self.head
            self.head = new_node
            return
        cur = self.head
        while cur.next and cur.next.data.dtb < sv.dtb:
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node  