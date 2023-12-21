def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    char_counts = char_count(text)
    sorted = []
    print(f"--- This report describes {book_path} ---")
    print(f"There are {words} words in {book_path}")
    print("")
    for i in char_counts:
        if i.isalpha() == True:
            sorted.append(i)
    sorted.sort()
    for i in sorted:
        print(f"The {i} character was found {char_counts[i]} times")    
    print("")
    print("--- END OF REPORT ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def char_count(text):
    ltext = text.lower()
    char_count_dic = {}
    chars = []
    
    for i in ltext:
       if i not in chars:
        chars.append(i)
    for char in chars:
        count = 0
        for i in ltext:
            if char == i:
                count += 1
        char_count_dic[char] = count
    return char_count_dic




def word_count(text):
    words = []
    words = text.split()
    return len(words)

main()