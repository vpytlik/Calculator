from parent import AbstractOperations


class Division(AbstractOperations):
    def division(self, x, y):
        if type(x) is float and type(y) is float:
            div = round(x, 2) / round(y, 2)
            return round(div, 2)
        else:
            div = x / y
            return round(div, 2)
        # else:
        #     print("Incorrect type of data")
