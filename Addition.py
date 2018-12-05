from parent import AbstractOperations


class Addition(AbstractOperations):
    def sum(self, x, y):
        if type(x) is float and type(y) is float:
            total = round(x, 2) + round(y, 2)
            return round(total, 2)
        elif type(x) is str and type(y) is str:
            total = x + y
            return total
        else:
            total = x + y
            return round(total, 2)

        # else:
        #     print("Incorrect type of data")
