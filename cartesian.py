import digestutils
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
            if not digestutils.tupleOverlaps(tuple):
                result.append(firstListElementToTuple + y)
    return result


def oneSolutionCartesian (lists, totalDifference, fileName):
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
        for y in oneSolutionCartesian(remainingLists, None, None):
            firstListElementToTuple = (x,)
            tuple = firstListElementToTuple + y
            if not digestutils.tupleOverlaps(tuple):
                if totalDifference and digestutils.isSolution(tuple, totalDifference):
                    print('We found solution ')
                    outputFile = open("output/one-solution-" + fileName, 'w')
                    digestutils.solutionToFile(tuple, outputFile)
                    outputFile.close()
                    return
                else:
                    result.append(firstListElementToTuple + y)
    return result
