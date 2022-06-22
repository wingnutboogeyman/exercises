# making it to python carnegie hall

class Pets():
    def __init__(self, animal, legs, nose, ears, coat, speed, fav_food):
        self.animal = animal
        self.legs = legs
        self.nose = nose
        self.ears = ears
        self.coat = coat
        self.speed = speed
        self.fav_food = fav_food

tomato = Pets("cat", 4, "pink", "pointy", "tuxedo", "very", "beef")
dunk = Pets("dog", 4, "black", "floppy", "white and caramel", "pretty", "lettuce")
tony = Pets("dog", 4, "black", "inbetween", "red", "super", "cat food")

print(tony.coat)
print(dunk.fav_food)
print(tomato.speed)