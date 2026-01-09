name = input("What's your name?:").strip().title()  #--> .strip() method remove todos os espaços em branco no começo e no final de uma palavra, não remove espaços
# em branco no meio

#end é um parametro contido na função print que pode ser editado para não pular linhas, por padrão o valor é end="\n"
#\n ==> pula uma linha
print('hello,' , end="")
print(name)

