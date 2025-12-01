userInput = input()
finalText = []
message = ""

#A ideia é jogar cada caractere numa lista e uni-los com base em condicionais, se tiver um : seguido de um ) na lista
#substituir por um rosto feliz

#print(a, b)

#Adicionando cada letra na lista
for character in userInput:
    if character == ":" or character == ")":
        continue
    else:
        finalText.append(character)
a , b = finalText.index(":") , finalText.index(")")
if (finalText[a] and finalText[b]) in finalText:
        finalText.append("🙂")
print("".join(finalText))







