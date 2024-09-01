
def add_numbers(num1, num2):
    """
    
    """
    return num1 + num2

def is_even(number):
    """
    
    """
    return number % 2 == 0

def reverse_string(text):
    """
    
    """
    return text[::-1]

def count_vowels(text):
    """
    
    """
    vowels = 'aeiou'
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

def calculate_factorial(n):
    """

    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)


def apply_decorator(func):
    """
    
    """
    def decorator_func(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return decorator_func

@apply_decorator
def example_function():
    return "Function executed"


def sort_by_age(list_of_tuples):
    """

    """
    return sorted(list_of_tuples, key=lambda x: x[1])


def merge_dicts(dict1, dict2):
    """

    """
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

class Car:
    def __init__(self, make, model, year):
        """
    
        """
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        """
        """
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2020)
    car.display_info()
