from material import Material


class Warehouse(object):
    def __init__(self, name):
        self.name = name
        self.materials = {}
        # creating dictionary to store the materials

    def store_material(self, material: Material, quantity: int):
        if quantity > material.max_capacity:
            # if the given quantity is grater than max capacity
            # there is no need to proceed with the checkings
            raise Exception("The given quantity cannot exceed the maximum capacity of the material")

        if material not in self.materials:
            self.materials[material] = 0
            # setting the initial quantity to 0

        if self.materials.get(material) + quantity > material.max_capacity:
            raise Exception("You're about to exceeded the maximum capacity")

        self.materials[material] = self.materials.get(material) + quantity
        return self  # in order to be able to chain methods

    def remove_material(self, material: Material, quantity: int):
        if quantity < 0:
            raise Exception("The quantity cannot be a negative number")
        if material not in self.materials:
            raise Exception("Material doesn't exist in " + self.name)
        if quantity > self.materials.get(material):
            raise Exception("The given quantity cannot exceed the maximum capacity of the material")

        self.materials[material] = self.materials.get(material) - quantity
        # subtracting the given amount from the amount we have, ant updating it in the dictionary

        if self.materials.get(material) == 0:
            del self.materials[material]
            # if the quantity already become 0, there is no need to keep item

        return self

    def move_material(self, target: "Warehouse", material: Material, quantity: int):
        self.remove_material(material, quantity)
        try:
            return target.store_material(material, quantity)
            # storing the material in the given target warehouse
            # while storing there can be errors if the max_capacity is about to be exceeded,
            # so we expect the material back and restore it back
        except Exception as e:
            self.store_material(material, quantity)
            # restoring removed material in the warehouse
            raise e
