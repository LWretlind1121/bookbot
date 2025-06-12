def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    words = file_contents.split()
    return len(words)


def main():
    print(f"{get_book_text("books/frankenstein.txt")} words found in the document")

main()

