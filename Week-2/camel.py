userInput = input('camelCase: ')

list_chars = []
def generate_list(str):
    """Take the user input and generate a list of each character"""
    for letter in str:
        list_chars.append(letter)
    return list_chars

positions = [] 
def find_index_char(list):
    """Find uppercase letter position in a list"""
    for char in list:
        if char.isupper():
            positions.append(list.index(char))
        else:
            continue
    return positions
print(find_index_char(generate_list(userInput)))

new_list_replace = []
def replace_upper(list):

