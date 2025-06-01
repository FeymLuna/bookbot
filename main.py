# Bookbot - boot.dev
import sys
sys.path.append("..")

from stats import get_book_text, word_count, character_count, list_dictionary, liste_sorted

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]

        print(f"============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print(f"----------- Word Count ----------")    
        print(f"Found {word_count(get_book_text(book))} total words")
        print(f"--------- Character Count -------")
        for char in liste_sorted(list_dictionary(character_count(get_book_text(book)))):
            print(f"{char['char']}: {char['num']}")

main()
