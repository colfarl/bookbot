
import sys
from stats import (
    get_num_words, 
    get_char_dict, 
    sort_char_dict
)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_chars(sorted_char_dict):
    for item in sorted_char_dict:
        if not item['char'].isalpha():
            continue
        print(f"{item["char"]}: {item["amt"]}")

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    sorted_char_dict = sort_char_dict(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    print_chars(sorted_char_dict)
    
if __name__ == "__main__":
    main()