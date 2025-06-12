import sys
from stats import get_num_words, get_letters, sort

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def mai():
    print(sys.argv)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        num = get_num_words(text)
        letters = get_letters(text)
        sorted_letters = sort(letters)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {num} total words")
        print("--------- Character Count -------")
        for item in sorted_letters:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")

main()

