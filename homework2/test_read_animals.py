import unittest
from read_animals import obtain_num_animals
class TestReadAnimals(unittest.TestCase):

    def test_get_num_animals(self):
        self.assertEqual(obtain_num_animals(2, 9), 2)
        self.assertEqual(obtain_num_animals(3, 3), 3)
        self.assertNotEqual(obtain_num_animals(1,4),4)
        self.assertRaises(ValueError, obtain_num_animals, 'animal', 5)
        self.assertRaises(TypeError, obtain_num_animals, None, 5)
        self.assertRaises(AssertionError, obtain_num_animals, 8, 5)
        self.assertRaises(AssertionError, obtain_num_animals, -3, 5)



if __name__ == '__main__':
    unittest.main()
