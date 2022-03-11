import time

def calculate_time(some_function):
    def wrapper():
        initialTime = time.time()
        some_function()
        finalTime = time.time()
        totalTime = finalTime - initialTime
        print(f'Total time {totalTime}')
    return wrapper

