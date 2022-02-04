# Import timeit module
import timeit
import sys

def canSum_memoization(targetSum, numbers, cacheDict):
    if targetSum in cacheDict.keys():
        return caceheDict[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0 :
        return False

    for number in numbers:
        remainder = targetSum - number
        if canSum_memoization(remainder,numbers, cacheDict) == True:
            cacheDict[targetSum] = True
            return True
    cacheDict[targetSum] = False
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
    cacheDict = {}
    t = timeit.timeit(lambda: print(canSum_memoization(targetNum, numbers, cacheDict)),number = 1)

    print("\nTime used to execute function is: ",t)
