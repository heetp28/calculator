#calculator
print('''
What do you want to do :-
+ to Add
- to Subtract
* to Multiply
/ to Divide''')

type1 =  input("\n")

#Add
if type1 == "+":
    number1 = input("\nWhat do you want to Add \n")
    number2 = input("+ \n")

    print(f"Ans. {float(number1) + float(number2)}")

#Subtract
elif type1 == "-":
    number1 = input("\nWhat do you want to Subtract \n")
    number2 = input("- \n")

    print(f"Ans. {float(number1) - float(number2)}")

#Multiply
elif type1 == "*":
    number1 = input("\nWhat do you want to Multiply \n")
    number2 = input("* \n")

    print(f"Ans. {float(number1) * float(number2)}")

#Divide
elif type1 == "/":
    number1 = input("\nWhat do you want to Divide \n")
    number2 = input("/ \n")

    print(f"Ans. {float(number1) / float(number2)}")

else:
    print(f"I didn't catch you")