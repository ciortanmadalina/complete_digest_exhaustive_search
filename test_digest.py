import unittest
import bruteforce

class BruteForceTest(unittest.TestCase):

    def test_no_permutations(self):
        input = []
        result = bruteforce.allPermutations(input)
        self.assertEqual(result , [])

    def test_1_permutation(self):
        input = [1]
        result = bruteforce.allPermutations(input)
        self.assertEqual(result , [1])

    def test_4_permutations(self):
        input = [1,2,3,4]
        result = bruteforce.allPermutations(input)
        self.assertTrue(len(result) == 24)

    def test_lengthsToPositions(self):
        input = [1, 3, 3, 2]
        result = bruteforce.cutpoints(input)
        self.assertEqual(result, [1, 4, 7])


    def test_lengthsToPositionsNoElement(self):
        input = []
        result = bruteforce.cutpoints(input)
        self.assertEqual(result, [])



if __name__ == '__main__':
    unittest.main()