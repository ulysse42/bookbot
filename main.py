from stats import *
from print_utils import *
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    sorted_char_count = get_sorted_char_count(char_count)
    print_intro()
    print_target(book_path)
    print_word_count(num_words)
    print_sorted_char_count(sorted_char_count)
    print_outro()


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
