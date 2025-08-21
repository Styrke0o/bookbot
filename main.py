import sys

def get_book_text():
	with open(sys.argv[1]) as f:
		file_contents = f.read()
		return file_contents


def main():
	if len(sys.argv)==2:
		book_path=sys.argv[1]
		text=get_book_text()
		output_message= "words found in the document" 	
		print(f"{word_count(text)} {output_message}")
		char=character_count(text)
		dict_sorted=dictionary_sort(char)
		print(f"============ BOOKBOT ============")
		print(f"Analyzing book found at {book_path}...")
		print(f"----------- Word Count ----------")
		print(f"Found {word_count(text)} total words")
		print(f"--------- Character Count -------")
		for i in dict_sorted:
			if i["char"].isalpha()==True:
				print(f"{i["char"]}: {i["num"]}") 
		print(f"============= END ===============")
	else:
		print(f"Usage: python3 main.py <path_to_book>")
		sys.exit(1)

from stats import word_count
from stats import character_count
from stats import dictionary_sort
main()
