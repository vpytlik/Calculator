from Addition import Addition
from Subtraction import Subtraction
from Multiplication import Multiplication
from Division import Division


def test_sum():
    my_test_calc = Addition()
    my_sum = my_test_calc.sum(12, 15)
    assert my_sum == 27


def test_sum_float():
    my_test_calc = Addition()
    my_sum = my_test_calc.sum(11, 2.22)
    assert my_sum == 13.22, 'The type of input data is float, incorrect rounding'


def test_sum_str():
    my_test_calc = Addition()
    my_sum = my_test_calc.sum('q', 'werty')
    assert my_sum == 'qwerty', 'The type of input data is string. It is concatenation'


def test_sub():
    my_test_calc = Subtraction()
    my_sub = my_test_calc.subtraction(2, 6)
    assert my_sub == -4


def test_sub_float():
    my_test_calc = Subtraction()
    my_sub = my_test_calc.subtraction(2.144, 6.122)
    assert my_sub == -3.98, 'The type of input data is float, incorrect rounding'


def test_mult():
    my_test_calc = Multiplication()
    my_mult = my_test_calc.multiplication(11, 6)
    assert my_mult == 66


def test_mult_float():
    my_test_calc = Multiplication()
    my_mult = my_test_calc.multiplication(1.123, 6.366)
    assert my_mult == 7.13, 'The type of input data is float, incorrect rounding'


def test_mult_str():
    my_test_calc = Multiplication()
    my_mult = my_test_calc.multiplication(3, 'qwa')
    assert my_mult == 'qwaqwaqwa', 'The type of input data is string. It is duplication of string'


def test_div():
    my_test_calc = Division()
    my_div = my_test_calc.division(66, 6)
    assert my_div == 11


def test_div_float():
    my_test_calc = Division()
    my_div = my_test_calc.division(66.663, 6)
    assert my_div == 11.11
