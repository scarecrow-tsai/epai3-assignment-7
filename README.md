# Assignment 7

This repo contains files for the 7th assignment on closures.

There are 2 files -

1. `assignment.py` : this file contains all the actual code.
2. `test_assignment.py` : this file contains all code to test the functions present in `assignment.py`.

## `assignment.py`

This file contains 4 functions.

1. `check_doc()`

   - This closure is used to check if a function's docstring has more than 50 characters.

2. `fibonacci()`

   - This function generates the fibonacci sequence starting from 1.

3. `global_counter(fn)`

   - A closure to keep a count of the number of times a function is called using a global dictionary.

4. `param_counter(fn, counters)`

   - A closure to keep a count of the number of times a function is called by passing a dictionary as an argument.

## `test_assignment.py`

This file contains test functions.

1.  `test_check_doc()`

    - Test to check the check_docstring() function.

2.  `test_fibonacci()`

    - Test to check the fibonacci() function.

3.  `test_global_counter()`

    - Test to check the global_counter() function.

4.  `test_param_counter()`

    - Test to check the param_counter() function.
