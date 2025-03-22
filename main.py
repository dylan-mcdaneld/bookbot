from stats import get_num_words, get_char_count, sorted_dicts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()





def main():

    if len(sys.argv) != 2:  # ensure a single argument is provided
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]

    contents = get_book_text(path_to_book)
    num_words = get_num_words(contents)


    char_counts = get_char_count(contents) # returns a dict

    char_counts_lst = sorted_dicts(char_counts)
    
    # Print results to console
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in char_counts_lst:
        if item["character"].isalpha():
            print(f"{item['character']}: {item['count']}")

    print("============= END ===============")

main()