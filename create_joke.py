def c_plus(number):
    print("{")
    for i in range(number + 1):

        print("    if (number == " + str(i) + ")")
        if is_prime(i):
            print("        return true;")
        else:
            print("        return false;")

    print("}")


def python(number):
    for i in range(number + 1):

        print("    if number == " + str(i) + ":")
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



num = int(input("How many number you want "))
# c_plus(num)
python(num)
