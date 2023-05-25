#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

# Define a name property for your Dog class. The name must be of type str and between 1 and 25 characters.
# If the name is invalid, the setter method should print() "Name must be string between 1 and 25 characters."

# Define a breed property for your Dog class.
# If the breed is invalid, the setter method should print() "Breed must be in list of approved breeds." 
# The breed must be in the following list of dog breeds:
class Dog:
    def __init__(self, name='', breed='Good Dog'):
        self.name = name
        self.breed = breed

    #------name property---------
    def get_dog_name(self):
        return self._name
    
    def dog_name(self, name):
        if (isinstance(name, str)) and (len(name) > 0) and len(name) < 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
    #--------------------------------

    #--------breed property---------pyt
    def get_breed(self):
        return self._breed
    
    def validate_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
    
    name = property(get_dog_name, dog_name)
    breed = property(get_breed, validate_breed)
    # name = property(dog_name)

#------------------------
print("Fido:")
fido = Dog("")
# Name must be string between 1 and 25 characters.
# Breed must be in list of approved breeds.
# # print(fido.breed)
# # Name must be string between 1 and 25 characters.
# # Breed must be in list of approved breeds.
# #AttributeError: 'Dog' object has no attribute '_breed'

# #fido does not meet criteria set by name and breed property (no name and no breed) 
# # so instance is not being created/allowed

print("Maggie:")
maggie = Dog(8008)
# Name must be string between 1 and 25 characters.
# Breed must be in list of approved breeds.

# #-------------------------
print("Chloe:")
chloe = Dog("Chloe")
chloe.dog_name("Chloe")
chloe.validate_breed("Heeler")
# #Breed must be in list of approved breeds.
# # print(chloe.breed)
# # Breed must be in list of approved breeds.

# #chloe meets name property validations but doesn't meet breed property criteria so instance is not being allowed/created

# # -------------------------
print("Beau:")
beau = Dog("Beau", "French Bulldog")
beau.validate_breed("French Bulldog")
beau.dog_name("Beau")
print(beau.name)
#Beau
print(beau.breed)
#French Bulldog

#beau meets both name and breed property criteria so instance is allowed and we're able to print his breed




