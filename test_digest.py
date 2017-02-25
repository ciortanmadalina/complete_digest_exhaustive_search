import unittest
import digest
class DigestTest(unittest.TestCase):

    def test_no_permutations(self):
        input = []
        result = digest.allPermutations(input)
        self.assertEqual(result , [])

    def test_1_permutation(self):
        input = [1]
        result = digest.allPermutations(input)
        self.assertEqual(result , [1])

    def test_4_permutations(self):
        input = [1,2,3,4]
        result = digest.allPermutations(input)
        self.assertTrue(len(result) == 24)

    def test_lengthsToPositions(self):
        input = [1, 3, 3, 2]
        result = digest.cutpoints(input)
        self.assertEqual(result, [1, 4, 7])


    def test_lengthsToPositionsNoElement(self):
        input = []
        result = digest.cutpoints(input)
        self.assertEqual(result, [])

    def test_positions_difference(self):
        input = [[1, 4, 8], [2, 5]]
        expected = [1, 1, 1, 2, 3]
        result = digest.positionsDifference(input)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()