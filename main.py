import sys
from stats import get_num_words, get_letters, sort

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(get_book_text(sys.argv[1]))} total words")
        print("--------- Character Count -------")
        for item in sort(get_letters(get_book_text(sys.argv[1]))):
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")

main()
