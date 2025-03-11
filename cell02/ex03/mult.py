number1 = int(input("Please Enter Your First Number"))
number2 = int(input("Please Input Your Secondary Number"))

result = number1 * number2
print(f"{number1}* {number2} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
