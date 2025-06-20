from stats import count_book_words, count_book_chars, sort_on, sort_chars
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    string_text_book = get_book_text(sys.argv[1])
    num_words = count_book_words(string_text_book)
    num_chars = count_book_chars(string_text_book)
    sorted_chars = sort_chars(num_chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for sorted_char in sorted_chars:
        print(f"{sorted_char['char']}: {sorted_char['num']}")
    print("============= END ===============")


main()