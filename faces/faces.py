name = input()

def faces(input):
        
    x = input.replace(":)", "🙂").replace(":(", "🙁")
    return x
    
        
print(faces(name))