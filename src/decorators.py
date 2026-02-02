from functools import wraps
from time import time
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*arg: Any, **kwarg: Any) -> Any:
            start_time = time()
            try:
                result = func(*arg, **kwarg)
                log_msg = f"{func.__name__} ok"
            except Exception as e:
                result = f"Inputs: {arg}, {kwarg}"
                log_msg = f"{func.__name__} error: {e}"
                if filename is None:
                    print(f"{log_msg}, answer: {result}")
                else:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_msg + "\n")
                exec_time = time() - start_time
                print(f"Время работы функции: {exec_time:.2f}\n")
                return result
            if filename is None:
                print(f"{log_msg}, answer: {result}")
            else:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(log_msg + "\n")
            exec_time = time() - start_time
            print(f"Время работы функции: {exec_time:.2f}\n")
            return result

        return inner

    return wrapper


@log()
def my_function(x: float, y: float) -> float:
    return x / y


my_function(6, 0)
