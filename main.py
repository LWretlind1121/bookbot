def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(words):
    num = words.split()
    return len(num)

def main():
    num = get_book_text("books/frankenstein.txt")
    print(f"{get_num_words(num)} words found in the document")
    

main()

