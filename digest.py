from functools import reduce
def getInputFromFile(filename):
    input = []
    f = open(filename, 'r')

    for line in f:
        input.append([int(i) for i in line.split(' ')])
    f.close()
    return input

input = getInputFromFile('input2')
print("Input : ",  input)

def allPermutations(inputArray):
    ''''
    Generates an array of all possible permutations of inputArray
    '''
    if len(inputArray) == 0 :
        return []
    if len(inputArray) == 1 :
        return inputArray
    if len(inputArray) == 2:
        return [inputArray, inputArray[:: -1]]
    result = []
    for i in range(len(inputArray)):
        #set one element and permute the rest
        currentElement = inputArray[i]
        remaining  = inputArray[:i] + inputArray [i + 1 :]
        for p in allPermutations(remaining):
            result.append([currentElement] + p)
    return result


def lengthsToPositions(inputArray):
    '''
    Generates DNA positions from subsequence lengths.
    For instance [1, 3, 3, 2]  produces [1, 4, 7, 9]
    :param inputArray:
    :return: positions array
    '''
    positions = []
    for i in range(len(inputArray)):
        if i == 0 :
            positions.append(inputArray[0])
        else:
            #add previous element to current element
            positions.append(positions[-1] + inputArray[i])
    return positions


def positionsDifference(allPositions):
    '''
    [[1, 4, 8], [2, 5]] will generate [1, 1, 1, 2, 3]
    :param allPositions:
    :return: the total sorted complete digest for  the input position sequences
    '''
    flatPositions = reduce( (lambda x, y: x + y), allPositions )
    flatPositions.sort()
    delta = [flatPositions[0]]
    for i in range(1, len(flatPositions)):
        delta.append(flatPositions[i]-flatPositions[i-1])
    delta.sort()
    return delta


def isSolution(kPositions, totalDifference):
    '''

    :param kPositions:
    :param totalDifference:
    :return: true when the difference for all k positions matches totalDifference
    '''
    return positionsDifference(kPositions) == totalDifference



def exhaustiveSearch(input):
    totalDifference = input[-1] #last line is the total complete digest
    print('tot', totalDifference)
    allKPermutations = []
    for i in range(len(input) - 1):
        permutations = allPermutations(input[i])
        positions = [lengthsToPositions(i) for i in permutations]
        allKPermutations.append(positions)

#print(positionsDifference([[1,4,8], [2,5]]))
#print(lengthsToPositions([1,3,3, 2]))
#print(allPermutations([1, 2, 3, 4]))
print(exhaustiveSearch(input))

