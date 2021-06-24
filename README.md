# Assignment 7

This repo contains files for the 7th assignment on closures.

## Lessons Covered

The following concepts were covered.

1. Global and Local Scopes
2. Non Local Scopes
3. Closures

## Assignment

1. Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable.

2. Write a closure that gives you the next Fibonacci number.

3. We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts.

4. Modify above such that now we can pass in different dictionary variables to update different dictionaries.

There are 2 files -

1. `assignment.py` : this file contains all the actual code.
2. `test_assignment.py` : this file contains all code to test the functions present in `assignment.py`.

## `assignment.py`

This file contains 4 functions.

### 1. `check_doc()`

- This closure is used to check if a function's docstring has more than 50 characters.

### 2. `fibonacci()`

- This function generates the fibonacci sequence starting from 1.

### 3. `global_counter(fn)`

- A closure to keep a count of the number of times a function is called using a global dictionary.

### 4. `param_counter(fn, counters)`

- A closure to keep a count of the number of times a function is called by passing a dictionary as an argument.

## `test_assignment.py`

This file contains test functions.

### 1. `test_check_doc()`

    - Test to check the check_docstring() function.

### 2. `test_fibonacci()`

    - Test to check the fibonacci() function.

### 3. `test_global_counter()`

    - Test to check the global_counter() function.

### 4. `test_param_counter()`

    - Test to check the param_counter() function.

### 5. `add(a, b)`

    - Function to add 2 numbers.

### 6. `mul(a, b)`

    - Function to multiply 2 numbers.

### 7. `div(a, b)`

    - Function to divide 2 numbers.
