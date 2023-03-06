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
            if parent.get_gender() == "M":
                child.set_father(parent)
            if parent.get_gender() == "F":
                child.set_mother(parent)
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

    def show_tree(self, root_id, indent=0):
        root: Human = self.get_unit_by_id(root_id)
        tree_str = " " * indent + f"{'└─── ' if indent > 0 else ''}" + str(root) + "\n"
        if len(root.children) > 0:
            for child in root.children:
                tree_str += self.show_tree(str(child.id_num), indent + 5)
        return tree_str
