# Import timeit module
import timeit

def fibonacci_memoization(n, cacheDict):
    if n in cacheDict.keys():
        return cacheDict[n]
    if n <= 2:
        return 1
    else:
        cacheDict[n] = fibonacci_memoization(n-1,cacheDict) + fibonacci_memoization(n-2,cacheDict)
        return cacheDict[n]

if __name__ == '__main__':
    # Initialize empty dictionary to pass as argument to our function.
    cacheDict = {}
    t = timeit.timeit(lambda: print(fibonacci_memoization(5, cacheDict)), number = 1)

    print("\nTime used to execute function is: ",t)
