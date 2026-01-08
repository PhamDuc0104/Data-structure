class LinkedList:
    def sap_xep_tang_dtb(self):
        if self.head is None:
            return
        p = self.head
        while p:
            q = p.next
            while q:
                if p.data.dtb > q.data.dtb:
                    p.data, q.data = q.data, p.data
                q = q.next
            p = p.next