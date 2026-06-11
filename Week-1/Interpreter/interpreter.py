user_input = input('Expression: ').split()

operators = ["+", "-", "*", "/"]
nums = []
operator = ""
def sum(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a , b):
    return a / b
def operations(a, b, operator):
    if operator == "+":
        return sum(a, b)
    elif operator == "-":
        return sub(a, b)
    elif operator == "*":
        return mult(a, b)
    elif operator == "/":
        return div(a, b)

#Transforming str to num
for character in user_input:
    if character not in operators:
        intNum = float(character)
        nums.append(intNum)
    elif character in operators:
        operator += character
print(operations(nums[0], nums[1], operator))




        

