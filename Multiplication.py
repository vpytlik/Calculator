from parent import AbstractOperations


class Multiplication(AbstractOperations):
    def multiplication(self, x, y):
        if type(x) is float and type(y) is float:
            mult = round(x, 2) * round(y, 2)
            return round(mult, 2)
        elif type(x) is str or type(y) is str:
            mult = x * y
            return mult
        else:
            mult = x * y
            return round(mult, 2)
        # else:
        #     print("Incorrect type of data")
