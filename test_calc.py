from Addition import Addition
from Subtraction import Subtraction
from Multiplication import Multiplication
from Division import Division
import pytest


@pytest.fixture
def calc_add():
    my_test_calc = Addition()
    return my_test_calc


@pytest.fixture
def calc_sub():
    my_test_calc = Subtraction()
    return my_test_calc


@pytest.fixture
def calc_mult():
    my_test_calc = Multiplication()
    return my_test_calc


@pytest.fixture
def calc_div():
    my_test_calc = Division()
    return my_test_calc


def test_sum(calc_add):
    # my_test_calc = Addition()
    my_sum = calc_add.sum(12, 15)
    assert my_sum == 27


def test_sum_float(calc_add):
    # my_test_calc = Addition()
    my_sum = calc_add.sum(11, 2.22)
    assert my_sum == 13.22, 'The type of input data is float, incorrect rounding'


def test_sum_str(calc_add):
    # my_test_calc = Addition()
    my_sum = calc_add.sum('q', 'werty')
    assert my_sum == 'qwerty', 'The type of input data is string. It is concatenation'


def test_sub(calc_sub):
    # my_test_calc = Subtraction()
    my_sub = calc_sub.subtraction(2, 6)
    assert my_sub == -4


def test_sub_float(calc_sub):
    # my_test_calc = Subtraction()
    my_sub = calc_sub.subtraction(2.144, 6.122)
    assert my_sub == -3.98, 'The type of input data is float, incorrect rounding'


def test_mult(calc_mult):
    # my_test_calc = Multiplication()
    my_mult = calc_mult.multiplication(11, 6)
    assert my_mult == 66


def test_mult_float(calc_mult):
    # my_test_calc = Multiplication()
    my_mult = calc_mult.multiplication(1.123, 6.366)
    assert my_mult == 7.13, 'The type of input data is float, incorrect rounding'


def test_mult_str(calc_mult):
    # my_test_calc = Multiplication()
    my_mult = calc_mult.multiplication(3, 'qwa')
    assert my_mult == 'qwaqwaqwa', 'The type of input data is string. It is duplication of string'


def test_div(calc_div):
    # my_test_calc = Division()
    my_div = calc_div.division(66, 6)
    assert my_div == 11


def test_div_float(calc_div):
    # my_test_calc = Division()
    my_div = calc_div.division(66.663, 6)
    assert my_div == 11.11
