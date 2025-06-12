from stats import get_num_words, get_letters, sort

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    num = get_num_words(text)
    letters = get_letters(text)
    sorted_letters = sort(letters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for item in sorted_letters:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()

