# Welcome to Python! This python script will teach the basics of Python Computing!
# We'll start with what "def" and "print()"  do.

# The 'def' keyword is used to define a new function in Python. We can define the introduction part:

def introduction():
    # Inside the function, we use the 'print()' function to display text on the screen.
    print("Hello! I'm your Python teacher. Let's start with the basics.")


def variables():
    # Variables are like boxes where you store information. You can give them names (also called labels) that remind you what they contain.
    # In programming, you often need to store information for later use. This is done using variables.
    # Note that the print() function here has a "new line" character. This is represented as print("\n")
    print("\nVariables:")
    # the "name" variable is defined.
    name = "Emi Yamashita"
    age = 17
    # The print() function has a prefix called f-string which allows us to insert values into strings directly.
    # To give the print() function the variables, we can put them in braces! (eg.  print(f"My name is {name}."))
    print(f"My name is {name} and I'm {age} years old.")

def data_types():
    print("\nData Types:")
    # You can connect 2 values, like a string and a variable with a comma.
    print("Integers:", 10)
    print("Floats:", 3.14)
    print("Strings:", "Hello, Python!")
    print("Booleans:", True)

def arithmetic_operations():
    # Arithmetic operations are performed by adding (+), subtracting (-), multiplying (*), or  dividing (/).
    print("\nArithmetic Operations:")
    print("Addition:", 5 + 3)
    print("Subtraction:", 5 - 3)
    print("Multiplication:", 5 * 3)
    print("Division:", 5 / 3)
    print("Modulus:", 5 % 3)
    print("Exponentiation:", 5 ** 3)

def comparison_operators():
    # Comparison Operators compare two values and return either True or False.
    print("\nComparison Operators:")
    print("Equal:", 5 == 3)
    print("Not Equal:", 5 != 3)
    print("Greater Than:", 5 > 3)
    print("Less Than:", 5 < 3)
    print("Greater Than or Equal:", 5 >= 3)
    print("Less Than or Equal:", 5 <= 3)

def logical_operators():
    print("\nLogical Operators:")
    print("And:", True and False)
    print("Or:", True or False)
    print("Not:", not True)

def control_flow():
    print("\nControl Flow:")
    # the "for i in range()" statement creates a loop that iterates over a sequence of numbers from 0 to (end-1).
    for i in range(1, 6):
        print(f"{i} x {i} = {i * i}")

def functions():
    print("\nFunctions:")
    # You can add a "def" function in another "def" function!
    def greet(name):
        # The return syntax returns the value of its argument. If no argument is provided, it returns None.
        return f"Hello, {name}!"
    print(greet("Emi"))

def main():
    # The main function acts as an entry point to your program. It's called when you run the script.
    # You can run your definitions by having the definition name followed by parentheses ().
    # For simplicity, we kept the arguments out. However, some pieces of code require arguments, or variables, to give to the contents of the definition.
    introduction()
    variables()
    data_types()
    arithmetic_operations()
    comparison_operators()
    logical_operators()
    control_flow()
    functions()

# This part can be tricky. This is how you call the main function so that it runs when you execute the script.
# The __name__ variable and the __main__ variable are special built-in constants that Python can run automatically.
if __name__ == "__main__":
    main()