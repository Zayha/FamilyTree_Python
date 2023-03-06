from file_l_s import Ser_file
from models.FamilyTree import FamilyTree
from models.Human import Human


class Service:

    def __init__(self) -> None:
        self.family_tree = FamilyTree()
        self.sf = Ser_file()

    def show_human(self, human):
        return f"{human}"

    def add_human(self, data):
        self.family_tree.add_to_family(Human(**data))

    def show_all(self):
        return self._create_str_from_list(self.family_tree)

    def _create_str_from_list(self, lst):
        result = "Общий список:\n"
        for i in lst:
            result += f"{i}\n"
        return result

    def get_unit_by_id(self, unit_id):
        for i in self.family_tree:
            if str(i.id_num) == unit_id:
                return i

    def add_child(self, child_id, parent_id):
        child: Human = self.get_unit_by_id(child_id)
        parent: Human = self.get_unit_by_id(parent_id)
        if child not in parent.children:
            parent.add_child(child)
            return True
        return False

    def save_tree(self, path: str):
        return self.sf.save_file(self.family_tree, path)

    def load_tree(self, path):
        temp_family = self.sf.load_file(path)
        if temp_family is not None:
            self.family_tree = temp_family
            return True
        else:
            return False

