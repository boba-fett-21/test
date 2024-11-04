# complex_script.py

import math
import random
import time
from datetime import datetime

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def normalize(self):
        max_val = max(self.data)
        min_val = min(self.data)
        self.data = [(x - min_val) / (max_val - min_val) for x in self.data]

    def calculate_mean(self):
        return sum(self.data) / len(self.data)

    def calculate_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            return sorted_data[n // 2]

class StringManipulator:
    def __init__(self, text):
        self.text = text

    def reverse_string(self):
        return self.text[::-1]

    def to_uppercase(self):
        return self.text.upper()

    def is_palindrome(self):
        cleaned_text = ''.join(e for e in self.text if e.isalnum()).lower()
        return cleaned_text == cleaned_text[::-1]

class RandomNumberGenerator:
    def __init__(self, seed=None):
        self.seed = seed
        if seed is not None:
            random.seed(seed)

    def generate_random_list(self, n, range_min, range_max):
        return [random.randint(range_min, range_max) for _ in range(n)]

    def shuffle_list(self, lst):
        random.shuffle(lst)
        return lst

def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def compute_square_roots(data):
    return [math.sqrt(x) if x >= 0 else None for x in data]

def find_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def complex_calculation(x, y, z):
    return (x ** 3 + y ** 2 - z) / (math.sin(x) + math.cos(y) + math.tan(z))

def current_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if self.start_time is None:
            raise ValueError("Timer was not started!")
        elapsed = time.time() - self.start_time
        self.start_time = None
        return elapsed

def main():
    # Data processing example
    processor = DataProcessor([2, 3, 5, 7, 11, 13])
    processor.normalize()
    print("Normalized data:", processor.data)
    print("Mean:", processor.calculate_mean())
    print("Median:", processor.calculate_median())

    # String manipulation example
    manipulator = StringManipulator("A man a plan a canal Panama")
    print("Reversed string:", manipulator.reverse_string())
    print("Uppercase:", manipulator.to_uppercase())
    print("Is palindrome:", manipulator.is_palindrome())

    # Random number generation example
    rng = RandomNumberGenerator(seed=42)
    random_numbers = rng.generate_random_list(5, 1, 100)
    print("Random numbers:", random_numbers)
    print("Shuffled numbers:", rng.shuffle_list(random_numbers))

    # Math functions
    print("Fibonacci sequence:", fibonacci(10))
    print("Factorial of 5:", factorial(5))
    print("Square roots:", compute_square_roots([0, 1, 4, 9, 16, 25, -4]))
    print("Primes up to 50:", find_primes(50))
    print("Complex calculation:", complex_calculation(1.5, 2.0, 0.5))

    # Timer usage
    timer = Timer()
    timer.start()
    time.sleep(1)
    elapsed_time = timer.stop()
    print("Elapsed time:", elapsed_time, "seconds")

if __name__ == "__main__":
    main()
