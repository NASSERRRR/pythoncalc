print('\n \n--------------------------------------------------------------------------------')
print('\n Calculator \n')
print("for addition type 1")
print("for subtraction type 2")
print("for multiplication type 3")
print("for division type 4")
print("for exponents type 5")
print("to exit the program type 0 \n")
option = int(input("Choose your type of calculation: "))
print("\n\n")
def Input():
    i1 = float(input("Enter the first number: "))
    return i1
def Input2():
    i2 = float(input("Enter the second number: "))
    return i2
while option != 0:
    if option == 1:
        print("The answer is:", Input() + Input2())
    elif option == 2:
        print("The answer is:", Input() - Input2())
    elif option == 3:
        print("The answer is:", Input() * Input2())
    elif option == 4:
        print("The answer is:", Input() / Input2())
    elif option == 5:
        print("The answer is:", Input() ** Input2())
    else:
        print("Error, you chose an invalid number")
    print('\n--------------------------------------------------------------------------------')
    option = int(input("\n Choose your next type of calculation: "))