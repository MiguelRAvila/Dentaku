from sys import exit

# Pretty simple what it does XD
def numberComp(item):
    try:
        float(item)
        return True
    except ValueError:
        return False

# Here we get the string (Parameter)
# Delete the white spaces
# Creates the list and

def getStack():
    print ("El programa recibe expresiones aritmeticas")
    print ("Por ejemplo: 5 + 2 * (2 + 1)")
    astring = input("Calcular: ")
    astring = astring.replace(" ", "")
    for item in astring:
        if item not in ["0", "1", "2", "3" , "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", ".", "(", ")"]:
            print ("El programa no acepta: " + item)
            exit()
    sStack = []
    for item in astring:
        sStack.append(item)
    count = 0
    while count < len(sStack) - 1:
        if numberComp(sStack[count]) and sStack[count + 1] == "(":
            print ("Debe existir un operador entre el parentesis y el resto de la expresión")
            exit()
        if numberComp(sStack[count]) and numberComp(sStack[count + 1]):
            sStack[count] += sStack[count + 1]
            del sStack[count + 1]
        elif numberComp(sStack[count]) and sStack[count + 1] == ".":
            try:
                x = sStack[count+2]
            except IndexError:
                print ("No esta escrito correctamente")
                exit()
            if numberComp(sStack[count + 2]):
                sStack[count] += sStack[count + 1] + sStack[count + 2]
                del sStack[count + 2]
                del sStack[count + 1]
        else:
            count += 1
    return sStack

# Make the operations
# Checkout errors

def mkOperation(n1, oper, n2):
    if oper == "+":
        return str(float(n1) + float(n2))
    elif oper == "-":
        return str(float(n1) - float(n2))
    elif oper == "*":
        return str(float(n1) * float(n2))
    elif oper == "/":
        try:
            n = str(float(n1) / float(n2))
            return n
        except ZeroDivisionError:
            print ("Jejeje no puedes hacer eso")
            exit()


# Handles the expression
# Short and better to understand

expression = getStack()
eCount = 0
P = ["(", ")"]
while len(expression) != 1:
    count = 0
    while count < len(expression) - 1:
        if expression[count] == "(":
            if expression[count + 2] == ")":
                del expression[count + 2]
                del expression[count]
        count += 1
    count = 0
    while count < len(expression) - 1:
        if expression[count] in ["*", "/"] and not (expression[count+1] in P or expression[count-1] in P):
            expression[count - 1] = mkOperation(expression[count - 1], expression[count], expression[count + 1])
            del expression[count + 1]
            del expression[count]
        count += 1
    count = 0
    while count < len(expression) - 1:
        if expression[count] in ["+", "-"] and not (expression[count+1] in P or expression[count-1] in P):
            expression[count - 1] = mkOperation(expression[count - 1], expression[count], expression[count + 1])
            del expression[count + 1]
            del expression[count]
        count += 1
    eCount += 1
    if eCount >= 1000:
        print ("Muy largo")
        exit()


print (float(expression[0]))