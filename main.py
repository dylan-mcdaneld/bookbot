from stats import get_num_words, get_char_count, sorted_dicts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()





def main():
    rel_path = "books/frankenstein.txt"
    contents = get_book_text(rel_path)
    num_words = get_num_words(contents)


    char_counts = get_char_count(contents) # returns a dict

    char_counts_lst = sorted_dicts(char_counts)
    
    # Print results to console
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {rel_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in char_counts_lst:
        if item["character"].isalpha():
            print(f"{item['character']}: {item['count']}")

    print("============= END ===============")

main()