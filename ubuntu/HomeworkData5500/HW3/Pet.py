

class Pet:
    species=None

    def __init__ (self,name,age,species):
        self.name = name
        self.age = age
        self.species = species
    def age_in_human_years(self):
        multiplier = {
            "dog": 7,
            "cat": 6,
            "rabbit": 8
        }
        multiplier = multiplier.get(self.species.lower(),1)
        return self.age * multiplier
    def average_lifespan(self):
        lifespan = {
            "dog": 13,
            "cat": 15,
            "rabbit": 9
        }
        return lifespan.get(self.species.lower(),"Unknown")

pet1 = Pet("Buddy", 5, "dog")
pet2 = Pet("Mittens", 3, "cat")
pet3 = Pet("Thumper", 2, "rabbit")

print(pet1.name, "'s age in human years is:", pet1.age_in_human_years())
print(pet2.name, "'s age in human years is:", pet2.age_in_human_years())
print(pet3.name, "'s age in human years is:", pet3.age_in_human_years())

print("The average lifespan of a", pet1.species, "is:", pet1.average_lifespan(), "years")
print("The average lifespan of a", pet2.species, "is:", pet2.average_lifespan(), "years")
print("The average lifespan of a", pet3.species, "is:", pet3.average_lifespan(), "years")


