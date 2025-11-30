userInput = input(":")
characters_list = []
emote_list = []
for character in userInput:
    if character != ":" and character != ")":
        characters_list.append(character)
    else:
        emote_list.append(character) #Adicionando os characteres dos emotes em uma lista separada
print(characters_list)
print(emote_list)

a = ["".join(emote_list)]
print(a)

