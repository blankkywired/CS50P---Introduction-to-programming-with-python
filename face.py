
userInput = input("")
characters_list = []
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

#Separando os characteres e adicionando em uma lista propria
myList = []
for char in userInput:
    if char == ":" or char == ")" or char == "(":
        myList.append(char)
#Agrupando characteres para formar emotes
emoteList = []
a = ""
b = []
if len(myList) % 2 == 0:
    for i in myList:
        if myList.index(i) % 2 != 0: #Compara o numero do indice para ver se é um valor par
            a =  myList[myList.index(i) - 1]
            a =  a + myList[myList.index(i)]
            emoteList.append(a)
print(emoteList)

#Convertendo emotes
simbol = ""
for emote in emoteList:
    if emote == ":)":
        simbol += "🙂"
    elif emote == ":(":
        simbol += "🙁"

