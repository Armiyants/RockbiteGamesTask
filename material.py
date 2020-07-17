class Material(object):
    def __init__(self, name: str, description: str, icon: str, max_capacity: int):
        self.name = name
        self.description = description
        self.icon = icon
        self.max_capacity = max_capacity
