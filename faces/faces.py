name = input()

def faces(input):
    x = input.replace(":)", "🙂")
    x = x.replace(":(", "🙁")

    #---- Other option ---#
    #x = input.replace(":)", "🙂").replace.(":(", "🙁") ---> #Passing replace mthod twice 
    return x

print(faces(name))