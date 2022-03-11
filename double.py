def doubler(some_func):
    def dWrapper():
        some_func()
        some_func()
    return dWrapper