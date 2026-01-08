class LinkedList:
    def xoa_sv(self, maSV):
        p = self.head
        prev = None
        while p:
            if p.data.maSV == maSV:
                if prev is None:
                    self.head = p.next  # xóa ở đầu
                else:
                    prev.next = p.next
                return True
            prev = p
            p = p.next
        return False