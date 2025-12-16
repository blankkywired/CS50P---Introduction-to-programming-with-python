

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #Todo
    x = ""
    for i in d:
        if i == "$":
            continue
        else:
            x += i
    x = float(x)
    return x
    

def percent_to_float(p):
    #todo
    y = ""
    for i in p:
        if i == "%":
            continue
        else:
            y += i
    y = float(y)
    y = y / 100
    return y


main()
