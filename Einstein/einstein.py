mass = int(input("m: "))
def energy(input):
    c = 300000000 * 300000000
    e = mass * c 
    return e
    
print(f"E: {energy(mass)}")