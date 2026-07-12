

def main():
   global user_time
   user_time = input('What time is it? ')
   HOUR = convert(user_time)

   if HOUR >= 7 and HOUR <= 8:
       print('breakfast time')
   elif HOUR >= 12 and HOUR <= 13:
       print('lunch time')
   elif HOUR >= 18 and HOUR <= 19:
        print('dinner time')



def convert(time):
    global time_convert
    #Dividindo os caracteres da entrada do usuario da variavel user_time e guardando em uma lista
    time_convert = time.split(":")
    #print(time_convert) #---> Exibe uma lista de cada par de numeros separados pelo :
    hour = 0
    for number in time_convert:
        number = int(number)
        #print(number)
        if number == int(time_convert[0]):
            minutes = number * 60
        else:
            minutes += int(time_convert[1])
    hour = minutes / 60
    hour = round(hour, 2)
    #print(hour)
    return hour
if __name__ == "__main__":
    main()

