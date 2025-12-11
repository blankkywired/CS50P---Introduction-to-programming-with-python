name = input()
def faces(input):
    
    x = name.replace(":(", "🙁")
    x = name.replace(":)", "🙂")
    return x
print(faces(name))