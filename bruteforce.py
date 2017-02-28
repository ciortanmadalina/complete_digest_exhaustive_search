
def getInputFromFile(filename):
    input = []
    f = open(filename, 'r')

    for line in f:
        input.append([int(i) for i in line.split(' ')])
    f.close()
    return input



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


def cutpoints(inputArray):
    '''
    Generates DNA positions from subsequence lengths.
    For instance [1, 3, 3, 2]  produces [1, 4, 7]
    This method omits the last element as it is not a cutpoint but the final
    position of the string. If we don't do this operation, all cutpoints will include as
    final element the length which is not a cutpoint.
    :param inputArray:
    :return: positions array
    '''
    positions = []
    for i in range(len(inputArray) - 1):
        if i == 0 :
            positions.append(inputArray[0])
        else:
            #add previous element to current element
            positions.append(positions[-1] + inputArray[i])
    return positions


def positionsDifference(allPositionsCutpoints, lastElement):
    '''
    ([1, 4, 8], [2, 5]) will generate [1, 1, 1, 2, 3]
    :param allPositions:
    :return: the total sorted complete digest for  the input position sequences
    '''
    flatPositions = []
    for position in allPositionsCutpoints:
        flatPositions.extend(position)
    #flatPositions = reduce( (lambda x, y: x + y), allPositions )
    flatPositions.append(lastElement)
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
    return positionsDifference(kPositions, sum(totalDifference) ) == totalDifference


def cartesian (lists):
    ''''
    This method generates recursively the cartesian product of input lists
    [ [[2,3],[4,5]], [[6,7],[8,9]] ] produces
    [([2, 3], [6, 7]), ([2, 3], [8, 9]), ([4, 5], [6, 7]), ([4, 5], [8, 9])]
    '''
    if lists == []: return [()]
    firstList = lists[0]
    remainingLists = lists[1:]
    result = []
    for x in firstList:
        for y in cartesian(remainingLists):
            firstListElementToTuple = (x,)
            result.append(firstListElementToTuple + y)
    return result

def exhaustiveSearch(input):
    totalDifference = input[-1] #last line is the total complete digest

    allKPermutations = []
    for i in range(len(input) - 1):
        permutations = allPermutations(input[i])
        positions = [cutpoints(i) for i in permutations]
        allKPermutations.append(positions)

    kCartesianProduct = cartesian(allKPermutations)
    print('We have ', len(kCartesianProduct), ' solutions' )
    for solution in kCartesianProduct:
        if isSolution(solution, totalDifference):
            print('Found solution :', solution)
            #as requested, we stop algorithm after finding the first solution
            #otherwise it would continue generating all solutions
            return solution






#########################
#RUN
#########################

input = getInputFromFile('input/example')
print("Input file: ",  input)
exhaustiveSearch(input)

