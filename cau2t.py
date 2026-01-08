def find_common_words(text_a, text_b):
    # Tách từ và tạo set
    words_a = set(text_a.lower().split())
    words_b = set(text_b.lower().split())
    
    # Giao của hai tập
    common = words_a & words_b
    
    return common