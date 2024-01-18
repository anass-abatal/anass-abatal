#Write a program that takes a number from the user input and represents that number with binary digits. Do the same thing with octal and hexadecimal conversions.

number=int(input("enter a number: "))
result=""
while number>=1:
    rest= number%2
    result= str(rest) + result
    number= int(number/2)
    print("The result is", result)
    