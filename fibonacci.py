# Import timeit module
import timeit

def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    t = timeit.timeit(lambda: print(fibonacci(20)), number = 1)

    print("\nTime used to execute function is: ",t)
