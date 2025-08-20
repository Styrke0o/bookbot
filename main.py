def get_book_text():
	with open('books/frankenstein.txt') as f:
		file_contents = f.read()
		return file_contents

def word_count(book):
	words = book.split()
	return len(words)

def main():
	text=get_book_text()
	output_message= "words found in the document" 	
	print(f"{word_count(text)} {output_message}")

main()
