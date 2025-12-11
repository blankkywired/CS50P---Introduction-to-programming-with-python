#Recriar função split em python
texto = input(': ')
#print(texto.split())


#Mostrando os indices de cada espço em branco
splitInList = []
indexChar = -1 #Contagem para exibir o indice contido em cada parte
#ocorrenciasEspaco = 0
for char in texto:
    if char == " ":
        splitInList.append(char)
        indexChar += 1
        print("Espaco apareceu no indice:" , indexChar)

    else:
        splitInList.append(char)
        indexChar += 1
#print(splitInList)
#print(ocorrenciasEspaco)

#Unir characteres
indexCharacter = 0
wordsList = []

word = ""
score = 0
while indexCharacter <= splitInList.index(splitInList[-1]): #basicamente um laço de repetição for
    print(splitInList[indexCharacter])
    if splitInList[indexCharacter] == " ":
        word = ""
        wordsList.append(word)

    elif splitInList[indexCharacter] != " ":
        word += splitInList[indexCharacter]
        if indexCharacter == splitInList.index(splitInList[-1]):
            wordsList.append(word)
    else:
        word += splitInList[indexCharacter] #Vai adicionando cada letra para a string 
        if indexCharacter == splitInList.index(splitInList[-1]):
            wordsList.append(word)

    indexCharacter += 1
print(wordsList)