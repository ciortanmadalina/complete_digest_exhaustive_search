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



def allPermutations(inputArray):
    ''''
    Brute force approach
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
