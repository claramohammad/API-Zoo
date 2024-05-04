import unittest
from zoo_models import Animal, Enclosure, Zoo  # Certifique-se de importar as classes corretamente

class TestZoo(unittest.TestCase):
    def test_feed_animal(self):
        animal = Animal("Leo", "Lion")
        animal.feed(10)
        self.assertEqual(animal.happiness, 10)

    def test_add_animal_to_wrong_enclosure(self):
        enclosure = Enclosure("Tiger")
        animal = Animal("Leo", "Lion")
        with self.assertRaises(ValueError):
            enclosure.add_animal(animal)

    def test_visitors(self):
        zoo = Zoo()
        enclosure = Enclosure("Lion")
        enclosure.add_animal(Animal("Leo", "Lion"))
        enclosure.add_animal(Animal("Simba", "Lion"))
        zoo.add_enclosure(enclosure)
        zoo.visitors(100)
        self.assertGreater(zoo.money, 0)

if __name__ == "__main__":
    unittest.main()
