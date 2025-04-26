import unittest
from assignment_06 import create_list, add_fruit, remove_second_fruit

class TestListOperations(unittest.TestCase):
    def test_list_operations(self):
        fruits = create_list()
        self.assertEqual(fruits, ['apple', 'banana', 'cherry', 'date', 'elderberry'])
        
        updated_fruits = add_fruit(fruits, 'fig')
        updated_fruits = remove_second_fruit(updated_fruits)
        
        self.assertEqual(updated_fruits, ['apple', 'cherry', 'date', 'elderberry', 'fig'])
        self.assertEqual(len(updated_fruits), 5)

if __name__ == "__main__":
    unittest.main()
