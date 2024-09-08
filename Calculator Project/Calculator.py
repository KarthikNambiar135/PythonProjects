from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2
def mutliply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def substract(n1, n2):
    return n1 - n2
operations = {
    '+' : add,
    '-' : substract,
    '*' : mutliply,
    '/' : divide
}
def calculator():
    continued = True
    f_num = int(input("Type the First Number: "))
    while continued:
        op = input("Input the Operator(+ - * /): ")
        l_num = int(input("Type the Last Number: "))
        result = operations[op](f_num, l_num)
        print(f"{f_num} {op} {l_num} is {result}")
        choice_input = True
        while choice_input:
            choice = input("Do you want to continue with the previous result, or perform a new"
                           "calculation?(yes, no or exit): ").lower()
            if choice == "exit":
                choice_input = False
                continued = False
                print("Program Exit.")
            elif choice == "yes":
                choice_input = False
                f_num = result
            elif choice == "no":
                choice_input = False
                continued = False
                print("\n" * 20)
                calculator()
            else:
                print("Invalid Input! Please Try Again.")
calculator()
