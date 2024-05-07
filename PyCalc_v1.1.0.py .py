print('''
▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
▐░█▀█░█░█░█▀▀░█▀█░█░░░█▀▀▌
▐░█▀▀░░█░░█░░░█▀█░█░░░█░░▌
▐░▀░░░░▀░░▀▀▀░▀░▀░▀▀▀░▀▀▀▌
▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
      ''')
     
print("Welcome To PyCalc v1.1.0")
number1 = int(input("enter a number:"))
sign = input("choose +, -, *, / :")
number2 = int(input("enter a number:"))
if sign == "+":
    result = number1 + number2
elif sign == "-":
    result = number1 - number2
elif sign == "*":
    result = number1 * number2
else: 
    result = number1 / number2
print(result)

flow = ""
while flow != "breakk":
    user = input("do you want to clear? :")
    if user == "clear":
        flow = "breakk"
        
    else:
        number = int(input("enter a number:"))
        sign1 = input("chosse: +, -, *, /")
        if sign1 == "+":
            result += number
        elif sign1 == "-":
            result -= number
        elif sign1 == "*":
            result *= number
        else:
            result /= number
        print(result)
        continue
    
    
    
