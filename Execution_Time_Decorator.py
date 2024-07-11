import time
import logging

logging.basicConfig(level=logging.INFO)

def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Execution time of {func.__name__}: {execution_time} seconds")
        return result
    return wrapper

@execution_time_decorator
def expensive_task():
    time.sleep(2)
    return "Task completed"

print(expensive_task())
