def c_plus(number= 10, variable_text= "number"):
    print("{")
    for i in range(number + 1):

        print(f"    if ({variable_text} == " + str(i) + ") {")
        if is_prime(i):
            print("        return true;")

        else:
            print("        return false;")

        print("    }")
    print("}")


def python(number= 10, variable_text= "number"):
    for i in range(number + 1):

        print(f"    if {variable_text}r == " + str(i) + ":")
        if is_prime(i):
            print("        return True")
        else:
            print("        return False")


def is_prime(p):
    if p <= 1:
        return False
    if p == 2:
        return True

    for i in range(2, int(p**0.5) + 1):
        if p % i == 0:
            return False
    return True


variable_name = input("Input your variable name: ")

if any(char.isdigit() for char in variable_name):
    raise ValueError("Name should be a string without numeric characters.")

num = int(input("How many number you want: "))

c_plus(num, variable_name)
# python(num, variable_name)
