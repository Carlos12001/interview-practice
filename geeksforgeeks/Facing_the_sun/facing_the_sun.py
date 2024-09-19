
class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        last_height = -1
        count = 0
        for i, h in enumerate(height):
            if last_height < h:
                count += 1 
                last_height = h
        return count

############ Test Cases ############
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.countBuildings([7, 4, 8, 2, 9]), 3)

    def test_2(self):
        self.assertEqual(self.solution.countBuildings([2, 3, 4, 5]), 4)


if __name__ == "__main__":
    unittest.main()