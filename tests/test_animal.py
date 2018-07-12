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
        """ tests that a new dog creation is an instance of dog and animal """
        buddy = Dog("Buddy")
        self.assertIsInstance(buddy, Dog)
        self.assertIsInstance(buddy, Animal)

    def test_getting_animal_name(self):
        """ tests that the get_name method returns the correct value """
        self.assertEqual(self.bob.get_name(), "Bob")
        self.assertNotEqual(self.bob.get_name(), "bob")
        self.assertNotEqual(self.bob.get_name(), "bill")

    def test_dog_can_walk(self):
        """ tests that a newly created dog object can call the walk method """
        murph = Dog("Murph")
        murph.walk()
        self.assertEqual(murph.speed, 0)
        murph.set_legs(4)
        murph.walk()
        self.assertEqual(murph.speed, 0.8)

    def test_animal_can_walk(self):
        """ tests that a newly created animal object can walk and errors will be raised if needed """
        test_animal = Animal()
        with self.assertRaises(ValueError):
            test_animal.walk()
        test_animal.set_legs(4)
        test_animal.walk()
        self.assertEqual(test_animal.speed, .4)

    def test_animal_can_set_species(self):
        """ tests that an animal object can set its species """
        self.bob.set_species("dog")
        self.assertEqual(self.bob.species, "dog")

    def test_animal_can_get_species(self):
        """ tests that an animal object can get its species """
        self.bob.set_species("doggo")
        self.assertEqual(self.bob.get_species(), "doggo")


    def test_animal_can_set_legs(self):
        """ tests that an animal object can set its legs """
        self.bob.set_legs(6)
        self.assertEqual(self.bob.legs, 6)


if __name__ == '__main__':
    unittest.main()