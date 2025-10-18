file_content = "Hello World"

def count_words(file_content):
    words = file_content.split()
    num_words = len(words)
    return num_words

def count_characters(file_content):
    standard = list(file_content.lower()) 
    char_dictionary = {}
    for char in standard:
        if char.isalpha():
            if char not in char_dictionary:
                char_dictionary[char] = 1
            else:
                char_dictionary[char] +=1
    return char_dictionary

char_dictionary = count_characters(file_content)
# print(char_dictionary)

def create_dictionary(char_dictionary):
    new_dict = []
    for key,value in char_dictionary.items():
        dictionary = {"char":key,"num": value}
        new_dict.append(dictionary)

    return new_dict

new_dict = create_dictionary(char_dictionary)
 

def sort_on(items):
    return items["num"]





