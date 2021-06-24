################################
# Question 1
################################
def check_doc():
    """
    This closure is used to check if a function's docstring has more than 50 characters.
    """
    num_chars = 50

    def inner(fn):
        if len(" ".join(fn.__doc__.split())) >= num_chars:
            return True
        else:
            return False

    return inner


################################
# Question 2
################################
def fibonacci():
    """
    This function generates the fibonacci sequence starting from 1.
    """
    x_1 = 0
    x_2 = 0

    def fib():
        nonlocal x_1, x_2
        if x_1 == 0 and x_2 == 0:
            x_1 = 1
        else:
            x_1, x_2 = x_1 + x_2, x_1

        return x_1

    return fib


################################
# Question 3
################################
g_counters = dict()


def global_counter(fn):
    """
    A closure to keep a count of the number of times a function is called using a global dictionary.
    """
    cnt = 0  # initially fn has been run zero times

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt = cnt + 1
        g_counters[fn.__name__] = cnt  # counters is global
        return fn(*args, **kwargs)

    return inner


################################
# Question 4
################################
def param_counter(fn, counters):
    """
    A closure to keep a count of the number of times a function is called by passing a dictionary as an argument.
    """
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt = cnt + 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)

    return inner
