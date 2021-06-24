import pytest
import os
import inspect
import re

import assignment


README_CONTENT_CHECK_FOR = [
    "global_counter",
    "fibonacci",
    "global_counter",
    "param_counter",
]


def test_assignment_readme_exists():
    """Checks if README file exists"""
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_assignment_readme_300_words():
    """Checks if README file has a minimum of 300 words"""
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert (
        len(readme_words) >= 300
    ), "Make your README.md file interesting! Add atleast 300 words"


def test_assignment_readme_proper_description():
    """Checks if README file has description of all the functions/classes."""
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert (
        READMELOOKSGOOD == True
    ), "You have not described all the functions/classes well in your README.md file"


def test_assignment_readme_file_for_more_than_10_hashes():
    """Checks if README file has proper formatting (minimum of 10 hashes)"""
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_assignment_indentations():
    """ Returns pass if used four spaces for each level of syntactically \
        significant indenting (spaces%4 == 2 and spaces%4 ==0).
    """
    lines = inspect.getsource(assignment)
    spaces = re.findall("\n +.", lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert (
            len(re.sub(r"[^ ]", "", space)) % 4 == 0
        ), "Your code indentation does not follow PEP8 guidelines"


def test_assignment_function_name_had_cap_letter():
    """test fails if Capital letter(s) used for function names"""
    functions = inspect.getmembers(assignment, inspect.isfunction)
    for function in functions:
        assert (
            len(re.findall("([A-Z])", function[0])) == 0
        ), "You have used Capital letter(s) in your function names"


def test_check_doc():
    """
    Test to check the check_docstring() function.
    """

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
    """
    Test to check the fibonacci() function.
    """
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
    """
    Test to check the global_counter() function.
    """
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
    """
    Test to check the param_counter() function.
    """
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
