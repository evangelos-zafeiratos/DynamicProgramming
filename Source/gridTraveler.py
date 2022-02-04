# Import timeit module
import timeit
import sys

def gridTraveler(m,n):
    if m == 1 and n == 1 :
        return 1
    elif m == 0 or n == 0 :
        return 0

    return gridTraveler(m-1,n) + gridTraveler(m, n-1)

if __name__ == '__main__':
    try:
        rows = int(input('Please enter the number of rows: '))
    except:
        print('You entered an invalid input.')
        sys.exit(1)
    try:
        cols = int(input('Please enter the number of columns: '))
    except:
        print('You entered an invalid input.')
        sys.exit(1)
    t = timeit.timeit(lambda: print(gridTraveler(rows,cols)), number = 1)

    print("\nTime used to execute function is: ",t)
