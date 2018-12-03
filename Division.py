from parent import AbstractOperations


class Division(AbstractOperations):
    def division(self, x, y):
        if x.isdigit() and y.isdigit():
            div = int(x) / int(y)
            return div
        else:
            print("Incorrect type of data")
