myList = ["hello", "world", "cs50p" , ":"]
# myList = [":", ")" , ":", "(" , ":" , ")" ]
#To-do
#Agrupar os characteres em pares caso o tamanho da lista seja um valor par
#Cada par de caracteres deve ter um indice dentro da lista
#Objetivo --> [":)", ":)", ":)"]

#Agrupando caracteres
emoteList = []
a = ""

if len(myList) % 2 == 0:
    for i in myList:
        if myList.index(i) % 2 != 0: #Compara o numero do indice para ver se é um valor par
            a =  myList[myList.index(i) - 1]
            a =  a + myList[myList.index(i)]
            emoteList.append(a)
print(emoteList)

