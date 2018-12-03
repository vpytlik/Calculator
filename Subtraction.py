from parent import AbstractOperations


class Subtraction(AbstractOperations):
    def subtraction(self, x, y):
        if x.isdigit() and y.isdigit():
            sub = int(x) - int(y)
            return sub
        else:
            print("Incorrect type of data")

