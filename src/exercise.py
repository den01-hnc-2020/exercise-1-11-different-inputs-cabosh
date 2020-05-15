def main():
    #write your code below this line
    string = str(input("Enter a string: "))
    integer = int(input("Enter an integer: "))
    Float = float(input("Enter a float: "))
    Boolean = input("Enter a boolean: ")

    print("You give the string  " + string)
    print("You gave the integer " + str(integer))
    print("You gave the float " + str(Float))

    if Boolean == "true":
        print("You gave the boolean " + Boolean)
    elif Boolean == "false":
        print("You gave the boolean " + Boolean)
    else:
        print("You didn't enter a Boolean!")

if __name__ == '__main__':
    main()
