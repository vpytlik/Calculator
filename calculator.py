from Addition import Addition
from Subtraction import Subtraction
from Multiplication import Multiplication
from Division import Division

my_add = Addition()
my_sub = Subtraction()
my_mult = Multiplication()
my_div = Division()


def main():
    while True:
        print("Welcome! Select operation:")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")

        operation = int(input())

        if operation == 1:
            x = input("Enter value for x:")
            y = input("Enter value for y:")
            sum_ = my_add.sum(x, y)
            print(sum_)
        elif operation == 2:
            x = input("Enter value for x:")
            y = input("Enter value for y:")
            sub = my_sub.subtraction(x, y)
            print(sub)
        elif operation == 3:
            x = input("Enter value for x:")
            y = input("Enter value for y:")
            mult_ = my_mult.multiplication(x, y)
            print(mult_)
        elif operation == 4:
            x = input("Enter value for x:")
            y = input("Enter value for y:")
            div = my_div.division(x, y)
            print(div)
        elif operation == 5:
            print("Goodbye")
            break
        else:
            print("Incorrect value of operation")


if __name__ == "__main__":
    main()









