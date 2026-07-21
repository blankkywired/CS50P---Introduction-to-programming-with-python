userInput = input('camelCase: ')

list_chars = []
def generate_list():
    """Take the user input and generate a list of each character"""
    for letter in userInput:
        list_chars.append(letter)
    return list_chars


def convert(list):
    new_list = []   
    for char in list:
        if char.isupper():
            char = char.lower()
            new_list.append("_")
            new_list.append(char)
        else:
            new_list.append(char)
    new_list = "".join(new_list)
    return new_list
print(convert(userInput))