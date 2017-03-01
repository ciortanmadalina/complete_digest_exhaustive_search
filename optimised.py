import numpy as np
import permutations as permutations_package
import cartesian as cartesian_package
import digestutils

def getInputFromFile(filename):
    input = []
    f = open(filename, 'r')

    for line in f:
        input.append([int(i) for i in line.split(' ')])
    f.close()
    return input


def exhaustiveSearch(input, generateAllSolutions):
    print("Running exhaustive search for input : ", input)
    totalDifference = input[-1] #last line is the total complete digest

    enzymeBitwisePermutations = []
    for i in range(len(input) - 1):
        permutations = permutations_package.permutationsNoDuplicates(input[i])
        positions = [digestutils.segmentsToBitewiseCutpoints(i) for i in permutations]
        enzymeBitwisePermutations.append(positions)


    if generateAllSolutions:
        bitwiseEnzymeCombinations = cartesian_package.completeCartesian(enzymeBitwisePermutations)

        outputFile = open("output/" + fileName, 'w')
        for tuple in bitwiseEnzymeCombinations:
            if digestutils.isSolution(tuple, totalDifference):
                digestutils.solutionToFile(tuple, outputFile)
        outputFile.close()
    else:
        cartesian_package.oneSolutionCartesian(enzymeBitwisePermutations, totalDifference, fileName)




#########################
#RUN
#########################

fileName = 'k3'
input = getInputFromFile("input/" + fileName)
exhaustiveSearch(input, False)

