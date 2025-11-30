myList = [":", ")" , ":", ")" , ":" , ")"]
#To-do
#Agrupar os characteres em pares caso o tamanho da lista seja um valor par
#Cada par de caracteres deve ter um indice dentro da lista
#Objetivo --> [":)", ":)", ":)"]


emoteList = []
a = ""
b = []
if len(myList) % 2 == 0:
    for i in myList:
        if myList.index(i) % 2 == 0: #Compara o numero do indice para ver se é um valor par
            b.append(myList[myList.index(i)])
            
print(b)
            


