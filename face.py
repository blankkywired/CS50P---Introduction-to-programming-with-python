userInput = input(">")
characters_list = []
emote_list = []
b = []

newInput = ""

#Format user input
for char in userInput:
    if char == " ":
        newInput += " "
    elif char != ":" and char != ")" and char != "(":
        newInput += char
    else:
        continue
print(newInput)  

#Adicionar characteres dos emotes
for character in userInput:
    characters_list.append(character)
    if character == ":" or character == ")" or character == "(":
        emote_list.append(character)




#print(characters_list)
#print(emote_list)
a = []
formateEmote = []
for simbol in emote_list:
    formateEmote.append(simbol)
for i in range(0, 1):
    if len(formateEmote) % 2 == 0:
        a.append("".join(formateEmote))
print(formateEmote)
#print(characters_list)
#print(emote_list)
c , d = formateEmote.index(":") , formateEmote.index(")")
print(c, d)
#Pqp eu odeio viver
for i in range(len(formateEmote)):
