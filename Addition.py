from parent import AbstractOperations


class Addition(AbstractOperations):
    def sum(self, x, y):
        if x.isdigit() and y.isdigit():
            total = int(x) + int(y)
            return total
        else:
            print("Incorrect type of data")
