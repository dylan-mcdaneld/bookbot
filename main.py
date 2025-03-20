from stats import get_num_words, get_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()





def main():
    rel_path = "books/frankenstein.txt"
    contents = get_book_text(rel_path)
    num_words = get_num_words(contents)
    print(f"{num_words} words found in the document")

    char_counts = get_char_count(contents)
    print(char_counts)


main()