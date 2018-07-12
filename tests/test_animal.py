import unittest
import sys
sys.path.append('../')
from animal import Animal
from animal import Dog


class TestAnimal(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bob = Dog("Bob")

    def test_animal_creation(self):
        self.assertIsInstance(self.bob, Dog)
        self.assertIsInstance(self.bob, Animal)

    def test_animal_can_set_legs(self):
        self.bob.set_legs(6)
        self.assertEqual(self.bob.legs, 6)

    


if __name__ == '__main__':
    unittest.main()