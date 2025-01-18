frankenstein = "books/frankenstein.txt"

def main(path_to_file):
    text = get_text(path_to_file)
    num_words = get_words(text)
    letters_dict = get_letters(text)
    print_report(path_to_file, num_words, letters_dict)
    

def print_report(path_to_file, num_words, letters_dict):
    alphabet = list('abcdefghijklmnoprstquvwxyz')
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{num_words} words found in the document\n")
    sorted_dict = {k: v for k, v in sorted(letters_dict.items(), key=lambda item: item[1], reverse=True)}
    for k, v in sorted_dict.items():
        if k in alphabet:
            print(f"The '{k}' character was found {v} times")
    print("--- End report ---")

def get_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_words(text):
    words = text.split()
    return len(words)

def get_letters(text):
    letters = {}
    words = text.lower()
    for letter in words:
        if letter not in letters.keys():
            letters[letter] = 1
        else:
            letters[letter] += 1
    
    return letters


main(frankenstein)