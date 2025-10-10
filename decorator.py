import time
def greet(func):
    def wrapper():
        print("Start")
        func()
        print("End")
    return wrapper

@greet
def say_hello():
    print("Hello Partner")

# say_hello()

def time_decorator(func):
    def time_calculate():
        start = time.time()               # start time
        print("Function Start")
        func()                            # actual function run
        end = time.time()                 # end time
        print("Function End")
        print("Execution time:", end - start, "seconds")
    return time_calculate

@time_decorator
def slow_func():
    time.sleep(2)
    print("Function Done")

slow_func()

