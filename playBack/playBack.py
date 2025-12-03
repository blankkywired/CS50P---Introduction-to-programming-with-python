
#Solução 1
#userInput = input("")
#splitText = userInput.split()
# print("...".join(splitText))


#Solução 2
userInput = input("")
finalText = ""
for caracter in userInput:
    if caracter == " ":
        finalText += "..."
    else:
        finalText += caracter
print(finalText)

