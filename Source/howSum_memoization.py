# Import timeit module
import timeit
import sys

def howSum_memoization(targetSum, numbers, cacheDict):
    if targetSum in cacheDict.keys():
        return cacheDict[targetSum]
    if targetSum == 0:
        numbersArray = list()
        return numbersArray
    if targetSum < 0 :
        return None

    for number in numbers:
        remainder = targetSum - number
        remainderResult = howSum_memoization(remainder, numbers, cacheDict)
        if remainderResult != None:
            remainderResult.append(number)
            cacheDict[targetSum] = remainderResult
            return remainderResult
    cacheDict[targetSum] = None
    return None

if __name__ == '__main__':
    try:
        targetSum = int(input('Please enter the target number: '))
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
    t = timeit.timeit(lambda: print(howSum_memoization(targetSum, numbers, cacheDict)),number = 1)

    print("\nTime used to execute function is: ",t)
