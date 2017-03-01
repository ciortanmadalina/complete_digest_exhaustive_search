import unittest
import optimised
import permutations as permutations_package

class OptimisedTest(unittest.TestCase):

    def test_no_permutations(self):
        input = []
        result = permutations_package.permutationsNoDuplicates(input)
        self.assertEqual(result , [])


    def test_no_duplicates(self):
        input = [2,2,2]
        result = permutations_package.permutationsNoDuplicates(input)
        self.assertEqual(result , [input])


    def test_1_permutation(self):
        input = [1]
        result = permutations_package.permutationsNoDuplicates(input)
        self.assertEqual(result , [1])

    def test_4_permutations(self):
        input = [1,2,3,4]
        result = permutations_package.permutationsNoDuplicates(input)
        self.assertTrue(len(result) == 24)

    def test_segmentToBitwiseCutpointsConverter(self):
        input = [1, 3, 3, 2, 1]
        result = optimised.bitewiseCutpointsToSegments(optimised.segmentsToBitewiseCutpoints(input))
        self.assertEqual(result, input.sort())

    def test_tuple_overlaps(self):
        input = ([1,0, 1],[0,0, 1])
        self.assertEqual(optimised.tupleOverlaps(input), True)

        input = ([1, 0, 1], [0, 1, 0])
        self.assertEqual(optimised.tupleOverlaps(input), False)


if __name__ == '__main__':
    unittest.main()