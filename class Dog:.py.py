class Dog:
    # Class attribute (shared by ALL instances)
    species = "canis familiaris"
    num_legs = 4
    num_ears = 2
    num_eyes = 2
    max_lifespan = 20

    # Constructor - spawning function
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    # Instance methods - shared by ALL instances
    def bark(self):
        return f"{self.name} says Woof!"

    def age_one_year(self):
        self.age = self.age + 1

    def live_forever(self):
        self.max_lifespan = 100000000000000

    def get_married(self, other_dog):
        child_dog_name = self.name[:2] + other_dog.name[:2]
        self.child = Dog(child_dog_name, self.color, 0)
        other_dog.child = self.child

    

bolt = Dog("Bolt", "white", 2)
coco = Dog("Coco", "brown", 10)
blueberry = Dog("Blueberry", "black", 2)

bolt.get_married(coco)

print(bolt.child) # <__main__.Dog object at 0x102a8de00>
print(bolt.child.name) # BoCo

print(coco.child.name)

print(bolt.child == coco.child)



