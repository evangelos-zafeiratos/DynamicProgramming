# Import timeit module
import timeit
import sys

def canSum(targetSum, numbers):
    if targetSum == 0:
        return True
    if targetSum < 0 :
        return False

    for number in numbers:
        remainder = targetSum - number
        if canSum(remainder,numbers) == True:
            return True
    return False

if __name__ == '__main__':
    try:
        targetNum = int(input('Please enter the target number: '))
    except:
        print('You entered an invalid input.')
        sys.exit(1)
    try:
        strNumbers = input('Please enter the list of numbers seperated by Space: ')
        numbers = [int(number) for number in strNumbers.split()]
    except:
        print('You entered an invalid input.')
        sys.exit(1)
    t = timeit.timeit(lambda: print(canSum(targetNum, numbers)),number = 1)

    print("\nTime used to execute function is: ",t)
