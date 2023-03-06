class FamilyTree:

    def __init__(self, **kwargs):
        self.family = []
        if "family" in kwargs:
            self.family = kwargs.get("family")

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.family):
            raise StopIteration
        member = self.family[self.index]
        self.index += 1
        return member

    def add_to_family(self, human):
        self.family.append(human)

    def set_family(self, family):
        self.family = family

    def del_from_family(self, human):
        self.family.remove(human)

    def get_family(self):
        return self.family
