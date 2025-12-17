import sys

from stats import (count_words,
    count_letters,
    sort_dict)



def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(file_path))} total words")
    print("--------- Character Count -------")
    report_list = (sort_dict(count_letters(get_book_text(file_path))))
    for item in report_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
