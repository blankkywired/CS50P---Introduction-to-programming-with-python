time_convert = input('What time is it?: ')

def main():
   HOUR = convert(time_convert)

   if HOUR >= 7 and HOUR <= 8:
       print('breakfast time')
   elif HOUR >= 12 and HOUR <= 13:
       print('lunch time')
   elif HOUR >= 18 and HOUR <= 19:
        print('dinner time')



def convert(time):
    global time_convert
    global list_char
    time_convert = time_convert.split(":")
    print(time_convert)
    hour = 0
    for number in time_convert:
        number = int(number)
        #print(number)
        if number == int(time_convert[0]):
            minutes = number * 60
        elif number == int(time_convert[1]):
            minutes += int(time_convert[1])
    hour = minutes / 60
    hour = round(hour, 2)
    print(hour)
    return hour
if __name__ == "__main__":
    main()