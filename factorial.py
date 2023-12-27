def factorial(n):
    if n < 0:
        raise ValueError("Factorial can only be computed for non-negative numbers!")
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    print(factorial(5))
    print(factorial(1))
    print(factorial(0))