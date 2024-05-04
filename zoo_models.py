class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.happiness = 0  # Neutral
    
    def feed(self, value):
        self.happiness += value

class Enclosure:
    def __init__(self, species):
        self.species = species
        self.animals = []
        self.conservation_status = "Bem cuidado"
    
    def change_status(self, new_status):
        self.conservation_status = new_status

    def add_animal(self, animal):
        if animal.species == self.species:
            self.animals.append(animal)
        else:
            raise ValueError("Espécie do animal não compatível com o recinto")
        
class Zoo:
    def __init__(self):
        self.enclosures = []
        self.money = 0

    def add_enclosure(self, enclosure):
        self.enclosures.append(enclosure)

    def visitors(self, visitors_number):
        happiness_rate = sum(animal.happiness for enclosure in self.enclosures for animal in enclosure.animals)
        conservation_rate = sum(1 for enclosure in self.enclosures if enclosure.conservation_status == "Bem cuidado")
        self.money += visitors_number * (happiness_rate + conservation_rate)
