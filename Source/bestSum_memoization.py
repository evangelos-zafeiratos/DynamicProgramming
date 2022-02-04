# Import timeit module
import timeit
import sys

def bestSum_memoization(targetSum, numbers,cacheDict):
    if targetSum in cacheDict.keys():
        return cacheDict[targetSum]
    if targetSum == 0:
        numbersArray = list()
        return numbersArray
    if targetSum < 0 :
        return None

    shortestCombination = None
    for number in numbers:
        remainder = targetSum - number
        remainderCombination = bestSum_memoization(remainder, numbers, cacheDict)
        if remainderCombination != None:
            combination = remainderCombination.copy()
            combination.append(number)
            if shortestCombination == None or len(combination) < len(shortestCombination):
                shortestCombination = combination
    cacheDict[targetSum] = shortestCombination
    print("The shortest combination for :", targetSum," is: ", shortestCombination)
    print(cacheDict)
    return shortestCombination

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
    t = timeit.timeit(lambda: print(bestSum_memoization(targetSum, numbers, cacheDict)),number = 1)

    print("\nTime used to execute function is: ",t)
