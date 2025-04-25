while True:
    a = input("Enter an Integer: ")
    try:
        number = int(a)
        print("Entered integer: ",number)
        break

    except ValueError:
        print("Please enter integer")
