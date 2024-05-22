def main():
    file = "books/frankenstein.txt"
    with open(file) as f:
        file_contents = f.read()
    num_words = word_count(file_contents)
    num_char_dict = char_count(file_contents)
    new_list = []
    for l in num_char_dict:
        new_list.append({"letter":l, "num":num_char_dict[l]})
    new_list.sort(reverse=True, key=sort_on)

    print("")
    print(f"--- Begin report of {file} ---")
    print(f"{num_words} words found in the document")
    print("")
    
    for entry in new_list:
        if entry["letter"].isalpha():
            print(f"The '{entry["letter"]}' character was found {entry["num"]} times")
    
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_dict = {}
    lower_case_text = text.lower()
    for letter in lower_case_text:
        if letter in char_dict:
            char_dict[letter] += 1
        else:
            char_dict[letter] = 1
    return char_dict

main()