import numpy as np
def getInputFromFile(filename):
    input = []
    f = open(filename, 'r')

    for line in f:
        input.append([int(i) for i in line.split(' ')])
    f.close()
    return input



def permutationsNoDuplicates(inputArray):
    ''''
    Generates an array of all possible permutations of inputArray
    '''
    if len(inputArray) == 0 :
        return []
    if len(inputArray) == 1 :
        return inputArray
    if len(inputArray) == 2:
        if inputArray[0] == inputArray [1]:
            return [inputArray]
        else:
            return [inputArray, inputArray[:: -1]]
    result = []
    previousElement = None #this will allow us to remove premutations
    for i in range(len(inputArray)):
        #set one element and permute the rest
        currentElement = inputArray[i]

        #if current element is the same as the one before, the permutations of all other elements
        #have been already generated
        if previousElement == currentElement:
            continue #we have already handled this case
        previousElement = currentElement


        remaining  = inputArray[:i] + inputArray [i + 1 :]
        for p in permutationsNoDuplicates(remaining):
            result.append([currentElement] + p)
    return result


def segmentsToBitewiseCutpoints(inputArray):
    '''
    Encodes the input array as a vector of DNA letters size with 1
    at the position where a cutpoint exists and 0 elsewhere
    For instance [1, 3, 3, 2, 1]  produces [0 1 0 0 1 0 0 1 0 1]

    This method omits the last element as it is not a cutpoint but the final
    position of the string. If we don't do this operation, all cutpoints will include as
    final element the length which is not a cutpoint.

    :param inputArray:
    :return: positions array
    '''
    positions = np.zeros(sum(inputArray),dtype=np.int )
    previousSum = 0
    for i in range(len(inputArray) - 1):
        positions[previousSum + inputArray[i] ] = 1
        previousSum += inputArray[i]

    return positions


def segmentsToPositions(inputArray):
    '''
    This method returns the positions in decimal from the bitwise form:
    [0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0]  gives [7, 16]
    :param inputArray:
    :return: segment sizes array from bitwise cutpoints input
    '''
    positions = []
    for i in range(len(inputArray)):
        if(inputArray[i] == 1) :
            positions.append(i)

    return positions

def bitewiseCutpointsToSegments(inputArray):
    '''
    This method is the inverse of segmentsToBitewiseCutpoints
    For instance for [0 1 0 0 1 0 0 1 0 1] it produces the sorted [1, 1, 2, 3, 3]

    This method will be used to check of the segments resulting from the
    combination of k lines match the total input difference
    :param inputArray:
    :return: segment sizes array from bitwise cutpoints input
    '''
    segments = []
    segmentSize = -1
    for bit in inputArray:
        if bit == 0:
            segmentSize +=1
        else:
            segments.append(segmentSize + 1)
            segmentSize = 0
    segments.append(segmentSize + 1) #add the last element
    segments.sort()
    return segments


def isSolution(tuple, totalDifference):
    '''
    :param kPositions:
    :param totalDifference:
    :return: true when the difference for all k positions matches totalDifference
    '''

    sum = 0
    for tupleElement in tuple:
        sum += np.array(tupleElement)

    return bitewiseCutpointsToSegments(sum) == totalDifference


def completeCartesian (lists):
    ''''
    This method generates recursively the cartesian product of input lists.

    It generates ALL possible solutions of tuples which don't overlap
    (we started with the assumption that 2 different enzymes can't get fixed
    at exactly the same position.

    Example:
    cartesian([ [[1,0, 1],[0,0, 1]], [[1,0, 0],[0,1,0]] ]) produces
    [([1, 0, 1], [0, 1, 0]), ([0, 0, 1], [1, 0, 0]), ([0, 0, 1], [0, 1, 0])]

    '''
    if lists == []: return [()]
    firstList = lists[0]
    remainingLists = lists[1:]
    result = []
    for x in firstList:
        for y in completeCartesian(remainingLists):
            firstListElementToTuple = (x,)
            tuple = firstListElementToTuple + y
            if not tupleOverlaps(tuple):
                result.append(firstListElementToTuple + y)
    return result


def tupleOverlaps(tuples):
    '''
    Example: ([1,0, 1],[0,0, 1]) overlap
    ([1,0, 1],[0,1, 0]) don't overlap
    :param tuples:
    :return: True if input tuples overalap, False otherwise
    '''
    sum = 0
    for tuple in tuples:
        sum += np.array(tuple)
    return len([x for x in sum if x > 1]) != 0

def solutionToFile(solution, file):
    print("Solution : ")
    file.write("\nSolution : \n")
    for line in solution:
        print(line, ' or segments of lengths : ', segmentsToPositions(line))
        file.write(str(line) +  ' or segments of lengths : ' + str(segmentsToPositions(line)) + '\n')
    print("\n")

def oneSolutionCartesian (lists, totalDifference):
    ''''
    This method generates recursively one single element of the cartesian product
    of input lists.


    Before assessing if a tuple is a potential solution, it filters out all
    tuples which overlap.
    (we started with the assumption that 2 different enzymes can't get fixed
    at exactly the same position.

    TotalDifference array is used to determine if a tuple is a solution,
    but it is also the discriminator between the original function call and the
    rest of recursive calls ( all recursive calls send totalDifference = None)

    Example:
    cartesian([ [[1,0, 1],[0,0, 1]], [[1,0, 0],[0,1,0]] ]) produces
    [([1, 0, 1], [0, 1, 0]), ([0, 0, 1], [1, 0, 0]), ([0, 0, 1], [0, 1, 0])]

    '''
    if lists == []: return [()]
    firstList = lists[0]
    remainingLists = lists[1:]
    result = []
    for x in firstList:
        for y in oneSolutionCartesian(remainingLists, None):
            firstListElementToTuple = (x,)
            tuple = firstListElementToTuple + y
            if not tupleOverlaps(tuple):
                if totalDifference and isSolution(tuple, totalDifference):
                    print('We found solution ')
                    outputFile = open("output/one-solution-" + fileName, 'w')
                    solutionToFile(tuple, outputFile)
                    outputFile.close()
                    return
                else:
                    result.append(firstListElementToTuple + y)
    return result




def exhaustiveSearch(input, generateAllSolutions):
    print("Running exhaustive search for input : ", input)
    totalDifference = input[-1] #last line is the total complete digest

    enzymeBitwisePermutations = []
    for i in range(len(input) - 1):
        permutations = permutationsNoDuplicates(input[i])
        positions = [segmentsToBitewiseCutpoints(i) for i in permutations]
        enzymeBitwisePermutations.append(positions)


    if generateAllSolutions:
        bitwiseEnzymeCombinations = completeCartesian(enzymeBitwisePermutations)

        outputFile = open("output/" + fileName, 'w')
        for tuple in bitwiseEnzymeCombinations:
            if isSolution(tuple, totalDifference):
                solutionToFile(tuple, outputFile)
        outputFile.close()
    else:
        oneSolutionCartesian(enzymeBitwisePermutations, totalDifference)






#########################
#RUN
#########################

fileName = 'k3'
input = getInputFromFile("input/" + fileName)
exhaustiveSearch(input, False)

