def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    counted_chars = count_characters(text)
    sorted_char_counts = chars_dict_to_sorted_list(counted_chars)
    print_report(path_to_file,num_words,sorted_char_counts)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    counted_chars ={}
    lowercase_text = text.lower()
    for character in lowercase_text:
        if character.isalpha():
            if character not in counted_chars:
                counted_chars[character] =1
            else: 
                counted_chars[character] +=1
    return counted_chars

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char":ch , "num":num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key= sort_on)
    return sorted_list


def print_report(path_to_file, num_words, sorted_char_counts):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{num_words} words found in the document\n")
    
    for item in sorted_char_counts:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")
    


main()