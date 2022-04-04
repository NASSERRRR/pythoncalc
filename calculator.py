print('\n \n--------------------------------------------------------------------------------')
print('\n Calculator \n')
print("for addition press 1")
print("for subtraction press 2")
print("for multiplication press 3")
print("for division press 4")
print("for exponents press 5")
print("to exit the program press 0 \n")


option = int(input("Choose your type of calculation: "))
print("\n\n")

while option != 0:
    if option == 1:
        a1 = float(input("Enter the first number: "))
        a2 = float(input("Enter the second number: "))
        af = a1 + a2
        print("The answer is {}".format(af))
    elif option == 2:
        s1 = float(input("Enter the first number: "))
        s2 = float(input("Enter the second number: "))
        sf = s1 - s2
        print("The answer is {}".format(sf))
    elif option == 3:
        m1 = float(input("Enter the first number: "))
        m2 = float(input("Enter the second number: "))
        mf = m1 * m2
        print("The answer is {}".format(mf))
    elif option == 4:
        d1 = float(input("Enter the first number: "))
        d2 = float(input("Enter the second number: "))
        df = d1 / d2
        print("The answer is {}".format(df))
    elif option == 5:
        p1 = float(input("Enter the first number: "))
        p2 = float(input("Enter the second number: "))
        pf = p1 ** p2
        print("The answer is {}".format(pf))
    else:
        print("Error, you chose an unassigned number")
    print('\n--------------------------------------------------------------------------------')
    option = int(input("\n Choose your next type of calculation: "))
