
userInput = input("")
newInput = ""


#Format user input
myList = []
for char in userInput:
    if char == " ":
        newInput += " "
    elif char != ":" and char != ")" and char != "(":
        newInput += char
    else:
        myList.append(char)
        
print(newInput)  

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

for char in userInput:
    if char == " ":
        newInput += " "
    elif char != ":" and char != ")" and char != "(":
        newInput += char
    else:
        newInput += emoteList[emoteList.index(char)]

    
text = userInput.split()
print(newInput)