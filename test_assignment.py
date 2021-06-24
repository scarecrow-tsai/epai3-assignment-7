import pytest
import assignment


def test_check_doc():
    def sample_correct():
        """
        This is docstring that is 50 characters long because why not hahahahahaha.
        """
        pass

    def sample_incorrect():
        """
        Small docstring.
        """
        pass

        assert (
            assignment.check_doc(sample_correct) == True
            and assignment.check_doc(sample_incorrect) == False
        )


def test_fibonacci():
    fib = assignment.fibonacci()
    first = fib()
    second = fib()
    third = fib()
    fourth = fib()

    assert first == 1 and second == 1 and third == 2 and fourth == 3


def mul(a, b):
    """
    A function to multiply 2 entities.
    """
    return a * b


def add(a, b):
    """
    A function to add 2 entities.
    """
    return a + b


def div(a, b):
    """
    A function to divide 2 entities.
    """
    return a / b


def test_global_counter():

    counted_add = assignment.global_counter(add)
    counted_mul = assignment.global_counter(mul)
    counted_div = assignment.global_counter(div)

    counted_add(1, 2)
    counted_mul(1, 2)
    counted_mul(1, 2)
    counted_div(1, 2)
    counted_div(1, 2)
    counted_div(1, 2)

    assert (
        assignment.g_counters["add"] == 1
        and assignment.g_counters["mul"] == 2
        and assignment.g_counters["div"] == 3
    )


def test_param_counter():
    counters = dict()

    counted_add = assignment.param_counter(add, counters)
    counted_mul = assignment.param_counter(mul, counters)
    counted_div = assignment.param_counter(div, counters)

    counted_add(1, 2)
    counted_mul(1, 2)
    counted_mul(1, 2)
    counted_div(1, 2)
    counted_div(1, 2)
    counted_div(1, 2)

    assert counters["add"] == 1 and counters["mul"] == 2 and counters["div"] == 3
