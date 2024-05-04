class Animal:
    def __innit__(self, name, species):
        self.name = name
        self.species = species
        self.hapiness = 0 #neutral
    
    def feed(self, value):
        self.hapiness += value

class Enclosure:
    def __innit__(self, species):
        self.species = species
        self.animals = []
        self.conservation_status = "Bem cuidado"
    
    def change_status(self, new_status):
        self.conservation_status = new_status

    def add_animal(self, animal):
        if animal.species == self.species:
            self.animals.append(animal)
        else:
            raise ValueError("Especie do animal não compativel com o recinto")
        
class Zoo:
    def __innit__(self):
        self.enclosures = []
        self.money = 0

    def add_enclosure(self, enclosure):
        self.enclosures.append(enclosure)

    def visitors(self, visitors_number):
        hapiness.rate = sum(animal.hapiness for enclosure in self.enclosures for animal in enclosure.animals)
        conservation_rate = sum(1 for enclosure in self.enclosures if enclosure.conservation_status == "Bem cuidado")
        self.money += visitors_number * (hapiness_rate + conservation_rate)