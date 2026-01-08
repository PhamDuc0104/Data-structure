
class LinkedList:
    def tim_sv(self, maSV):
        p = self.head
        while p:
            if p.data.maSV == maSV:
                return p.data
            p = p.next
        return None
