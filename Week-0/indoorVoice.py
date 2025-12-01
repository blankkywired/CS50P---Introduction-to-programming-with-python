alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_higher = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#Criar uma função que pegue o indice de uma letra em relação a uma lista de letras 
# e substituir essa letra pelo mesmo indice porem de uma letra minuscula de outro alfabeto


def indoor(text):
    finalText = ""
    splitText = text
    for caracter in splitText:
        if caracter == " ":
            finalText += " "
        else:
            indexChar = alphabet_higher.index(caracter)
            finalText += alphabet_lower[indexChar]
    return finalText

name = input()
print(indoor(name))                      

