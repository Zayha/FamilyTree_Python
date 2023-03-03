from file_l_s import Ser_file


class FamilyTree:

    def __init__(self, **kwargs):
        self.sl = Ser_file()
        self.family = []
        if "family" in kwargs:
            self.family = kwargs.get("family")

    def __str__(self):
        return f"В составе дерева {len(self.family)} персон(а)"

    def add_to_family(self, human):
        self.family.append(human)

    def set_family(self, family):
        self.family = family

    def save_tree(self, path="outTree"):
        self.sl.save_file(self.family, path)
