# Import timeit module
import timeit
import sys

def bestSum(targetSum, numbers):
    if targetSum == 0:
        numbersArray = list()
        return numbersArray
    if targetSum < 0 :
        return None

    shortestCombination = None
    for number in numbers:
        remainder = targetSum - number
        remainderCombination = bestSum(remainder, numbers)
        if remainderCombination != None:
            remainderCombination.append(number)
            if shortestCombination == None or len(remainderCombination) < len(shortestCombination):
                shortestCombination = remainderCombination
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
    t = timeit.timeit(lambda: print(bestSum(targetSum, numbers)),number = 1)

    print("\nTime used to execute function is: ",t)
