import allure


def step(func):
    @allure.step(f"{func.__module__}.{func.__name__}")
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
