from abc import ABCMeta, abstractmethod


class AbstractOperations:
    __metaclass__ = ABCMeta

    def division(self, x, y):
        pass

    def multiplication(self, x, y):
        pass

    def subtraction(self, x, y):
        pass

    def sum(self, x, y):
        pass
