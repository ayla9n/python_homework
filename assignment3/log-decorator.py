import logging


#Task 1: Writing and Testing a Decorator

# one time setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        logger.log(logging.INFO, f"function: {func.__name__}\n")
        logger.log(logging.INFO, f"positional parameters: {list(args) if args else 'none'}\n")
        logger.log(logging.INFO, f"keyword parameters: {kwargs if kwargs else 'none'}\n")
        logger.log(logging.INFO, f"return: {return_value}\n")
        return return_value
    return wrapper

@logger_decorator
def greeting():
    return("Hello World!")


greeting()

@logger_decorator
def test_args(*args):
    return True 

test_args("what", 67, "the", "sigma")


@logger_decorator
def test_kwargs(**kwargs):
    return logger_decorator

test_kwargs(name="puppy", age=5, color="golden")

