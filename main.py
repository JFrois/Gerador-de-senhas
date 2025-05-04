def hello_mensage():
    print("Hello, weolcome to our program!")
    
def goodbye_mensage():
    print("Thank you for using our program!")
    
def information_mensage():
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    caracter = int(input("Please enter how many carater do you want in your password: "))
    print(f"Hello, {name}, you are {age} years old and you want a password with {caracter} characters.")
    
def main():
    hello_mensage()
    information_mensage()
    goodbye_mensage()
    
if (__name__ == "__main__"):
    main()