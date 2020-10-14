print("----------------------------------------------")
print("")
print("             Even / Odd Detection")
print("")
print("                   0 to exit")
print("")
print("----------------------------------------------")
print("")

again = 1

while again == 1:
    userinput = input("Enter a positive whole number: ")
    num = int(userinput)
    eo = num % 2

    if num == 0:
        again = 0
    else:
        if eo == 0:
            print(f"The number {num} is even.")
            print("")
        else:
            print(f"The number {num} is odd.")
            print("")

print("Bye!")