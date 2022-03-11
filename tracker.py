def func_counter(some_func):
    def counter_func(y):
        some_func(y)
        counter_func.counter = counter_func.counter + 1

    counter_func.counter = 0
    return counter_func

@func_counter
def foo(y):
    return y+2**3-34

foo(1)
foo(1)
foo(1)
foo(1)
foo(1)
foo(1)
foo(1)
foo(1)
foo(1)

print(foo.counter)