import unittest
from assignment_02 import calculate_area

class TestRectangleArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(calculate_area(5, 3), 15)
        self.assertEqual(calculate_area(10, 2), 20)
        self.assertEqual(calculate_area(7, 7), 49)
        self.assertEqual(calculate_area(0, 10), 0)

if __name__ == "__main__":
    unittest.main()
