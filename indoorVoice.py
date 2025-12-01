#Solução 1
#name = input()
#name = name.lower()
#print(name)

#Solution 2 
alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_higher = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']




def indoor(text):
    finalText = ""
    splitText = text
    for caracter in splitText:
        if caracter == " ":
            finalText += " "
        elif not caracter in alphabet_higher:
            finalText += caracter
        else:
            indexChar = alphabet_higher.index(caracter)
            finalText += alphabet_lower[indexChar]
    return finalText

name = input()
print(indoor(name))                      

