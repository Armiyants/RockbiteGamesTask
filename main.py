from material import Material
from warehouse import Warehouse

icon = Material("Iron", "Hi, I am Iron, not Ironman", "This is icon of Iron", 500)


warehouse1 = Warehouse("First Warehouse")
warehouse2 = Warehouse("Second Warehouse")
warehouse2.store_material(icon, 400)
warehouse1.store_material(icon, 20)\
    .move_material(warehouse2, icon, 10)
# print(warehouse1.materials.get(icon))
# warehouse1.remove_material(icon, 30)
print(warehouse1.materials.get(icon))



