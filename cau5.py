class LinkedList:
    def liet_ke_lonhon5(self):
        p = self.head
        while p:
            if p.data.dtb >= 5:
                print(f"{p.data.maSV} - {p.data.tenSV} - {p.data.dtb}")
            p = p.next