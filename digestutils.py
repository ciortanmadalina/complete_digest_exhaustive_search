import numpy as np


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