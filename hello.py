# from flask import Flask
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start = time.time()
        function()
        end = time.time()
        print(f"The {function.__name__} speed is {end - start} seconds")

    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()