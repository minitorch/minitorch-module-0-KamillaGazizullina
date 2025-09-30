"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.

def mul(x: float, y: float) -> float:
    return x * y


def id(x: float) -> float:
    return x


def add(x: float, y: float) -> float:
    return x + y


def neg(x: float) -> float:
    return -x


def lt(x: float, y: float) -> float:
    return 1.0 if x < y else 0.0


def eq(x: float, y: float) -> float:
    return 1.0 if x == y else 0.0


def max(x: float, y: float) -> float:
    return x if x > y else y


def is_close(x: float, y: float) -> bool:
    return abs(x - y) < 1e-2


def sigmoid(x: float) -> float:
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    else:
        return math.exp(x) / (1.0 + math.exp(x))


def relu(x: float) -> float:
    return x if x > 0 else 0.0


def log(x: float) -> float:
    return math.log(x)


def exp(x: float) -> float:
    return math.exp(x)


def inv(x: float) -> float:
    return 1.0 / x


def log_back(x: float, d: float) -> float:
    # derivative of log(x) = 1/x, multiplied by d
    return d / x


def inv_back(x: float, d: float) -> float:
    # derivative of 1/x = -1/x^2, multiplied by d
    return -d / (x * x)


def relu_back(x: float, d: float) -> float:
    # derivative of relu(x) = 1 if x > 0 else 0, multiplied by d
    return d if x > 0 else 0.0


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map: применяем функцию к каждому элементу списка.
def map(fn, lst):
    return [fn(x) for x in lst]

# - zipWith: берём два списка и функцию, и объединяем элементы из двух списков с помощью этой функции.
def zipWith(fn, lst1, lst2):
    return [fn(x, y) for x, y in zip(lst1, lst2)]

# - reduce: сводим список к одному значению с помощью функции (напр, суммируем все элементы списка).
def reduce(fn, lst, start):
    result = start
    for x in lst:
        result = fn(result, x)
    return result

#
# Use these to implement
# - negList : negate a list
def negList(lst):
    return map(lambda x: -x, lst)

# - addLists : add two lists together
def addLists(lst1, lst2):
    return zipWith(lambda x, y: x + y, lst1, lst2)

# - sum: sum lists
def sum(lst):
    return reduce(lambda x, y: x + y, lst, 0.0) #Если не указать начальное значение, reduce будет использовать первый элемент списка как начальное значение, что может привести к ошибкам при пустом списке

# - prod: take the product of lists
def prod(lst):
    return reduce(lambda x, y: x * y, lst, 1.0)


# TODO: Implement for Task 0.3.
