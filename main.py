from stats import count_words, count_characters, create_dictionary, sort_on
import sys

def get_book_text(path_to_file):

    with open(path_to_file) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_content = get_book_text(sys.argv[1])
        
        num_words = count_words(file_content)

        char_dictionary = count_characters(file_content)

        sorted_list = create_dictionary(char_dictionary)

        sorted_list.sort(reverse=True, key=sort_on)


        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        
        for word in sorted_list:
            char = word["char"]
            num = word["num"]
            print(f"{char}: {num}")
        print("============= END ===============")


main()