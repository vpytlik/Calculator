from parent import AbstractOperations


class Subtraction(AbstractOperations):
    def subtraction(self, x, y):
        if type(x) is float and type(y) is float:
            sub = round(x, 2) - round(y, 2)
            return round(sub, 2)
        else:
            sub = x - y
            return round(sub, 2)
        # else:
        #     print("Incorrect type of data")

