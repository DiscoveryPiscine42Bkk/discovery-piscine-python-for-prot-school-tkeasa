number = input("Give me a number: ")
if '.' in number:
    try :
        num = float(number)
        if num.is_integer():
            print("This number is an integer.")
        else:
            print("This number is a decimal.")
    except ValueError:
        print("Please enter a valid number.")
else:
    print("This number is an integer.")
