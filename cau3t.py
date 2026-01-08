def longest_word_from_chars(chars, dictionary):
    from collections import Counter
    
    char_count = Counter(chars)
    longest = ""
    
    for word in dictionary:
        word_count = Counter(word)
        # Kiểm tra xem có đủ ký tự không
        if all(word_count[c] <= char_count[c] for c in word_count):
            if len(word) > len(longest):
                longest = word
    
    return longest