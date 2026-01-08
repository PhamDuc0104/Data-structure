def xep_loai(self, dtb):
    if dtb <= 3.6: 
        return "Yếu"
    elif 5.0 <= dtb < 6.5:  
        return "Trung bình"
    elif 6.5 <= dtb < 7.0: 
        return "Trung bình khá"
    elif 7.0 <= dtb < 8.0: 
        return "Khá"
    elif 8.0 <= dtb < 9.0: 
        return "Giỏi"
    elif dtb >= 9.0: 
        return "Xuất sắc"
    else:  
        return "Yếu"