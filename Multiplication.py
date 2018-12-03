from parent import AbstractOperations


class Multiplication(AbstractOperations):
    def multiplication(self, x, y):
        if x.isdigit() and y.isdigit():
            mult = int(x) * int(y)
            return mult
        else:
            print("Incorrect type of data")
